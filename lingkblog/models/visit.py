'''
@Descripttion: 访问记录表 visits
@version: v1.0
@Author: JalanJiang
@Date: 2019-06-07 12:03:02
@LastEditTime: 2019-06-07 12:31:48
'''
from lingkblog.models.base import Base
from lingkblog import db

from sqlalchemy import Column, Integer, String


class Visit(Base, db.Model):
    
    __tablename__ = 'visits'
    id            = Column(Integer, primary_key=True, comment='访问记录ID')
    ip            = Column(String(19), comment='访问者ip地址')
    page_url      = Column(String(19), comment='访问页面地址')
    # 待定 1-文章，2-主页，3-个人页
    page_type     = Column(Integer, comment='访问页面类型')
    article_id    = Column(Integer, comment='访问文章ID')
