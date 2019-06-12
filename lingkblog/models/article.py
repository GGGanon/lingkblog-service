'''
@Descripttion: 文章数据表 articles（其他周边数据：点赞、评论、阅读量、访问记录（按天））
@version: v1.0
@Author: JalanJiang
@Date: 2019-06-07 11:12:59
@LastEditTime: 2019-06-12 17:22:51
'''
from sqlalchemy import Column, Integer, String, Text, JSON

from lingkblog import db
from lingkblog.models.base import Base
from lingkblog.models.query_with_soft_delete import QueryWithSoftDelete


class Article(Base, db.Model):

    query_class = QueryWithSoftDelete

    __tablename__    = 'articles'
    id               = Column(Integer, primary_key=True, comment='文章ID')
    account_id       = Column(Integer, comment='发布者账号ID')
    title            = Column(String(99), comment='文章标题')
    summary          = Column(Text, comment='文章概要')
    content_type     = Column(Integer, comment='文章编辑内容类型，1-Markdown，2-富文本')
    content          = Column(Text, comment='文章主体内容')
    content_markdown = Column(Text, comment='Markdown 文本内容，当 content_type=1 时存在')
    word_count       = Column(Integer, default=0, comment='文章字数')
    read             = Column(Integer, default=0, comment='阅读次数')
    category_id      = Column(Integer, default=0, comment='所属分类。0-未分类')
    tags             = Column(JSON, comment='标签')
    # TODO: 待定，是否需要冗余
    # like          = Column(Integer, comment='点赞次数')
    # 缩略图
    status        = Column(Integer, default=2, comment='文章状态。1-已发布，2-未发布，3-已撤回')

    _status_publish = 1
    _status_draft   = 2
    _status_recall  = 3

    @property
    def status_publish(self):
        return Article._status_publish

    @property
    def status_draft(self):
        return Article._status_draft

    @property
    def status_recall(self):
        return Article._status_recall