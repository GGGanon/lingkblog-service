'''
@Descripttion: 文章数据表 articles（其他周边数据：点赞、评论、阅读量、访问记录（按天））
@version: v1.0
@Author: JalanJiang
@Date: 2019-06-07 11:12:59
@LastEditTime: 2019-06-07 12:14:02
'''
from sqlalchemy import Column, Integer, String, Text

from lingkblog import db
from lingkblog.models.base import Base


class Article(Base, db.Model):
    __tablename__ = 'articles'
    id            = Column(Integer, primary_key=True, comment='文章ID')
    account_id    = Column(Integer, comment='发布者账号ID')
    title         = Column(String(99), comment='文章标题')
    summary       = Column(Text, comment='文章概要')
    content       = Column(Text, comment='文章主体内容')
    word_count    = Column(Integer, comment='文章字数')
    read          = Column(Integer, comment='阅读次数')
    category_id   = Column(Integer, comment='所属分类')
    tags          = Column(String(99), comment='标签')
    # TODO: 待定，是否需要冗余
    # like          = Column(Integer, comment='点赞次数')
    # 缩略图
    status        = Column(Integer, comment='文章状态。1-已发布，2-未发布，3-已撤回')