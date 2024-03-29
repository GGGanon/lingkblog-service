'''
@Description: 模型基类
@Version: v1.0
@Author: JalanJiang
@Date: 2019-06-05 18:43:05
@LastEditTime: 2019-06-06 01:14:46
'''
import datetime
from sqlalchemy import Column, Integer, String, DateTime
from lingkblog import db

class Base():
    created_at = Column(DateTime, default=datetime.datetime.now, comment='创建时间')
    updated_at = Column(DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now, comment='更新时间')
    deleted_at = Column(DateTime, nullable=True, comment='软删除标志，记录删除时间')