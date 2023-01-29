import datetime

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Sites(Base):
    __tablename__ = "sites"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    data = Column(String)
    extracted_data = Column(String)
    last_update = Column(DateTime, default=datetime.datetime.utcnow())


class Queue(Base):
    __tablename__ = "queue"

    id = Column(Integer, primary_key=True)
    description = Column(String)
    medias = Column(String)
