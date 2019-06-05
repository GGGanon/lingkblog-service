'''
@Description: 用户账号模型
@Version: v1.0
@Author: JalanJiang
@Date: 2019-06-05 12:23:31
@LastEditTime: 2019-06-05 14:20:24
'''
from sqlalchemy import Column, Integer, String
from app import db


class Account(db.Model):
    __tablename__ = 'accounts'
    id            = Column(Integer, primary_key=True)
    name          = Column(String(12))
    email         = Column(String(50), unique=True)
    password      = Column(String(50))
    role_id       = Column(Integer)
    scope         = Column(String(250))
    status        = Column(Integer)