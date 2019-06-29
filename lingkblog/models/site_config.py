'''
@Descripttion: 站点配置信息
@version: v1.0
@Author: JalanJiang
@Date: 2019-06-29 23:43:43
@LastEditTime: 2019-06-30 00:22:48
'''
from sqlalchemy import Column, Integer, String, Text, JSON

from lingkblog import db
from lingkblog.models.base import Base
from lingkblog.models.query_with_soft_delete import QueryWithSoftDelete


class SiteConfig(Base, db.Model):

    query_class = QueryWithSoftDelete

    __tablename__ = 'site_config'
    id            = Column(Integer, primary_key=True, comment='配置ID')
    title         = Column(String(99), default='LingKBlog', comment='站点标题')
    subtitle      = Column(String(99), default='LingKBlog 是棒棒的博客', comment='站点二级标题')
    description   = Column(Text, default='博客 | LingKBlog', comment='站点描述')
    page_size     = Column(Integer, default=10, comment='每页显示数据量')
    friends       = Column(JSON, nullable=True, comment='友链')