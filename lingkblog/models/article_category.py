'''
@Descripttion: 文章分类模型
@version: v1.0
@Author: JalanJiang
@Date: 2019-06-10 16:35:30
@LastEditTime: 2019-06-10 16:39:32
'''
from lingkblog.models.base import Base
from lingkblog import db

from sqlalchemy import Column, Integer, String


class ArticleCategory(Base, db.Model):
    __tablename__ = 'article_categories'
    id = Column(Integer, primary_key=True, comment='文章分类ID')
    name = Column(String(19), comment='文章分类名称')