'''
@Descripttion: 文章控制器
@version: v1.0
@Author: JalanJiang
@Date: 2019-06-07 21:43:07
@LastEditTime: 2019-06-10 16:31:03
'''
from flask import g

from lingkblog import db
from lingkblog.services.base import Base
from lingkblog.models.article import Article as ArticleModel


class Admin(Base):

    def index(self):
        '''
        @descripttion: 获取文章列表
        @param query string title        文章标题
        @param query int    content_type 文章分类ID
        @param query string tag          标签
        @return: 
        '''
        pass

    def show(self):
        '''
        @descripttion: 获取文章详情
        @param path int artcile_id 文章ID
        @return: 
        '''
        pass

    def store(self):
        '''
        @descripttion: 发布文章
        @param {type} 
        @return: 
        '''
        # TODO: 参数验证

        account_id       = g.account_id
        title            = self.request.form['title']
        summary          = self.request.form['summary']
        content_type     = self.request.form['content_type']
        content          = self.request.form['content']
        content_markdown = self.request.form['content_markdown']
        # TODO: word_count 计算
        word_count  = 0
        category_id = self.request.form['category_id']
        tags        = self.request.form['tags']

        # 新增文章
        article_obj = ArticleModel(
            account_id=account_id,
            title=title,
            summary=summary,
            content_type=content_type,
            content=content,
            content_markdown=content_markdown,
            word_count=word_count,
            category_id=category_id,
            tags=tags
        )
        db.session.add(article_obj)
        db.session.commit()

        return self.return_success({
            'id': article_obj.id,
            'account_id': article_obj.account_id,
            'title': article_obj.title,
            'summary': article_obj.summary,
            'content_type': article_obj.content_type,
            'content': article_obj.content,
            'content_markdown': article_obj.content_markdown,
            'word_count': article_obj.word_count,
            'read': article_obj.read,
            'category_id': article_obj.category_id,
            'tags': article_obj.tags,
            'status': article_obj.status
        })

    def delete(self):
        '''
        @descripttion: 删除文章
        @param path int 文章ID
        @return: 
        '''
        pass


