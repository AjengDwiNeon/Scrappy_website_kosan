from os import link
from pydantic import BaseModel
from typing import Optional, List


class RequestCIF(BaseModel):
    cif: str = None


class detail_bgt(BaseModel):
    link: str = None
    title: str  = None
    alamat: str  = None
    jenis_kos: str  = None
    kecamatan: str  = None
    pelihara_binatang: str  = None
    detail_deskripsi: str  = None
    


class ResponseCIF(BaseModel):
    cif_list: List[detail_bgt]