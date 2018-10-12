# coding: utf-8

from sqlalchemy import Column, String, Integer

from sqlalchemy_django import SQLAlchemy

db = SQLAlchemy(bind_key='linkflood')


class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    age = Column(Integer)