import json
from nturl2path import url2pathname
from operator import itemgetter
from urllib import response
import requests
from bs4 import BeautifulSoup
import pandas as pd
from random import randint
from time import sleep
import re
import psycopg2
from soupsieve import select
from sympy import content
from tqdm import tqdm
from sqlalchemy.types import Integer, Text, String, DateTime
from sqlalchemy import create_engine
import warnings 
def how_to_scrap():
    warnings.filterwarnings('ignore')
    url_page = 'https://www.cari-kos.com/search?keywords=Jakarta'
    response = requests.get(url_page, verify=False)
    if response.status_code == 200:
        all_links = []
        html = response.text
        soup = BeautifulSoup(html, 'html5lib')
        kos = soup.select('div.search-listing-box')
        print('url', url_page)
        print('Jumlah article:', len(kos))
        for i in tqdm(range(len(kos)), "get Links"):    
            all_links.append({
            "link": kos[i].select_one('a').attrs['href'].strip(),
            "title": kos[i].select_one('h3').text.strip()
            #"addres": kos[i].select_one('div.address-text').text.strip(),
            #"Harga": kos[i].select_one('div.price-box').text.strip(),
            #"fasilitas": [x.text for x in kos[i].select('label')]
        })
    else:
        print('eror')

    return all_links

