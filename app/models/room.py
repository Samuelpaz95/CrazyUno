from sqlalchemy import Column, Integer, String

from .db import db


class Room(db.Model):
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True)
    code = Column(String(6), unique=True)
