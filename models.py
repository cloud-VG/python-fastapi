from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.sqlite import DATETIME
from database import Base


class Song(Base):
    __tablename__ = "songs"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    duration = Column(Integer)
    time = Column(DATETIME)


class Podcast(Base):
    __tablename__ = 'podcasts'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    duration = Column(Integer)
    time = Column(DATETIME)

    host = Column(String)
    participants = Column(String)


class AudioBook(Base):
    __tablename__ = 'audiobooks'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    duration = Column(Integer)
    time = Column(DATETIME)

    author = Column(String)
    narrator = Column(String)
