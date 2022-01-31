from sqlalchemy import create_engine, Column, Integer, String, Sequence, Float,PrimaryKeyConstraint, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.sql import *
from pydantic import BaseModel


#buat tabel
Base = declarative_base()
class database(Base):
    __tablename__ = "data_kosan_baru"
    link = Column(Integer, primary_key=True)
    title = Column(String)
    alamat = Column(String)
    jenis_kos = Column(String)
    kecamatan = Column(String)
    pelihara_binatang = Column(String)
    detail_deskripsi = Column(String)
Base.metadata.create_all(database)
Base.metadata.create_all(DbModel)

class detail_bgt(BaseModel):
    link: str = None
    title: str = None
    alamat: str = None
    jenis_kos: str = None
    kecamatan: str = None
    pelihara_binatang: str = None
    detail_deskripsi: str = None


class ResponseModel(BaseModel):
    cif_list: list[detail_bgt]