from email import message
from unittest import result
from apps.helper import Log
from apps.schemas import BaseResponse
from apps.schemas.SchemaCIF import RequestCIF, ResponseCIF
from apps.helper.ConfigHelper import encoder_app
from main import PARAMS
#from apps.models.LoanModel import Loan
from apps.models.DbModel import dbmodel
import json
from nturl2path import url2pathname
from operator import itemgetter
from urllib import response
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
from sqlalchemy.types import Integer, Text, String, DateTime
from sqlalchemy import create_engine
import warnings
import re

SALT = PARAMS.SALT.salt


class ControllerKosan(object):
    #method buat scrap link and title
    @classmethod
    def how_to_scrap(cls):
        warnings.filterwarnings('ignore')
        url_page = 'https://www.cari-kos.com/search?keywords=Jakarta'
        response = requests.get(url_page, verify=False)
        if response.status_code == 200:
            all_links = []
            html = response.text
            soup = BeautifulSoup(html, 'html5lib')
            kos = soup.select('div.search-listing-box')
            print('url', url_page)
            print('Jumlah  kos:', len(kos))
            for i in tqdm(range(len(kos)), "get Links"):
                item = all_links.append({
                    "link": kos[i].select_one('a').attrs['href'].strip(),
                    "title": kos[i].select_one('h3').text.strip()
                })
        else:
            print('eror')
        result = BaseResponse()
        result.status = 200
        result.message = "Success"
        result.data = all_links
        return result

    @classmethod
    #method for get detail berita
    def getdetail(cls):
        detail = []
        urlq = cls.how_to_scrap()
        for i in range(len(urlq.data)):
            url = urlq.data[i]['link']
            details = urlq.data[i]['title']
            # print(url)
            req = requests.get(url)
            # print(req.status_code)
            soup = BeautifulSoup(req.content, 'html.parser')
            items = soup.select('div.left-box-detail text')
            lokasi_kos = soup.select_one('div.detail-location-type')
            alamat = soup.select_one('div.address').text
            harga = soup.select_one('div.price-box').text.replace('Mulai',' ')
            xharga = re.findall('[0-9]+', harga)
            detail_lokasi_kos = {}
            for tr in lokasi_kos.select('tr'):
                try:
                    tr_split = tr.text.split(' : ')
                    detail_lokasi_kos[tr_split[0].strip()] = tr_split[1].strip()
                except:
                    pass
                detail_deskripsi = soup.select_one('div.detail-description').text.strip()
                regex = re.compile(r'[\n\r\t]')
                detail_deskripsi = regex.sub(' ', detail_deskripsi)
                #detail_deskripsi = ''.join([str(elem) for elem in detail_deskripsi])
                #detail_deskripsi = re.sub(r'[^ \w\.]', '', detail_deskripsi).lower()
            result = {
                "link": url,
                'title': details,
                "alamat": alamat,
                "harga": xharga,
                "jenis_kos": detail_lokasi_kos['Jenis Kos'],
                "Kecamatan": detail_lokasi_kos['Kecamatan'],
                "Pelihara_Binatang": detail_lokasi_kos['Pelihara Binatang'],
                "detail_deskripsi": detail_deskripsi
            }
            detail.append(result)
            print(detail)
        return detail
    @classmethod
    def get_kos_kota(cls,kota: str):
        result = BaseResponse
        result.status = 400
        url2 = 'https://www.cari-kos.com/search?keywords={kota}'
        listkota=[]
        for in range(20):
            url1 = f'https://www.cari-kos.com/search?keywords={kota}'
            req = requests.get(url1)
            soup2 = BeautifulSoup(req.content, 'html.parser')
            'div.search-listing-box'




    @classmethod
    #buat simpan data scrap ke db
    def simpan_data(cls):
        input_detail = cls.getdetail()
        # panjang_detail = len(input_detail)
        result = BaseResponse()
        result.status = 200
        for i in range(len(input_detail)):
            try:
                #save to db
                data_kosan = dbmodel()
                data_kosan.link = input_detail[i]['link']
                data_kosan.title = input_detail[i]['title']
                data_kosan.alamat = input_detail[i]['alamat']
                data_kosan.jenis_kos = input_detail[i]['jenis_kos']
                data_kosan.kecamatan = input_detail[i]['Kecamatan']
                data_kosan.pelihara_binatang = input_detail[i]['Pelihara_Binatang']
                data_kosan.detail_deskripsi = input_detail[i]['detail_deskripsi']
                data_kosan.save()
                result.status = 200
                result.message = input_detail[i]['url'] + " berhasil"
            except Exception as e:
                 print(e)
                 result.status = 400
                 result.message = " failed " + input_detail[i]['url'] + " Gagal"
                 #continue
            return result







