from lingkblog.models.base import Base
from lingkblog import db

from sqlalchemy import Column, String, Integer


class Operation(Base, db.Model):
    
    __tablename__ = 'operations'
    id            = Column(Integer, primary_key=True, comment='操作记录ID')
    account_id    = Column(Integer, comment='操作者账号ID')
    account_name  = Column(String(9), comment='操作者姓名')
    summary       = Column(String(19), comment='操作概要')
    description   = Column(String(99), comment='操作具体描述')