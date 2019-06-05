'''
@Description: 用户账号模型
@Version: v1.0
@Author: JalanJiang
@Date: 2019-06-05 12:23:31
@LastEditTime: 2019-06-06 00:40:28
'''
from sqlalchemy import Column, Integer, String
import json

from lingkblog.models.base import Base
from lingkblog import db


class Account(Base, db.Model):
    __tablename__ = 'accounts'
    id            = Column(Integer, primary_key=True)
    name          = Column(String(12))
    email         = Column(String(50), unique=True)
    password      = Column(String(50))
    role_id       = Column(Integer)
    scope         = Column(String(250))
    status        = Column(Integer)

    def __init__(self, name, email, password, role_id, scope=dict(), status=1):
        self.name     = name
        self.email    = email
        # TODO: 加密处理
        self.password = password
        self.role_id  = role_id
        self.scope    = json.dumps(scope) # json格式存储
        self.status   = status