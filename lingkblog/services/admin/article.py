'''
@Descripttion: 文章控制器
@version: v1.0
@Author: JalanJiang
@Date: 2019-06-07 21:43:07
@LastEditTime: 2019-06-12 15:26:24
'''
from flask import g, jsonify
import json

from lingkblog import db
from lingkblog.services.base import Base
from lingkblog.models.article import Article as ArticleModel
from lingkblog.exceptions.api_exception import APIException
from lingkblog.common.validators.store_article_form import StoreArticleForm
from lingkblog.exceptions.api_exception import APIException


class Article(Base):

    def index(self):
        '''
        @descripttion: 获取文章列表
        @param query int    page         页码
        @param query int    limit        每页数量
        @param query string title        文章标题
        @param query int    content_type 文章分类ID
        @param query string tag          标签
        @return: 
        '''
        pass

    def show(self, id):
        '''
        @descripttion: 获取文章详情
        @param path int artcile_id 文章ID
        @return: 
        '''
        article_obj = ArticleModel.query.filter_by(id=id).first()
        if not article_obj:
            raise APIException(err_key='article_not_found')
        
        return self.return_success({
            'id'              : article_obj.id,
            'title'           : article_obj.title,
            'content_type'    : article_obj.content_type,
            'status'          : article_obj.status,
            'word_count'      : article_obj.word_count,
            'content'         : article_obj.content,
            'content_markdown': article_obj.content_markdown,
            'summary'         : article_obj.summary,
            'tags'            : article_obj.tags,
            'read'            : article_obj.read
        })

    def store(self):
        '''
        @descripttion: 发布文章
        @param {type} 
        @return: 
        '''
        # 参数验证
        store_article_form = StoreArticleForm.from_json(self.request.json)
        if not store_article_form.validate():
            raise APIException(err_msg=store_article_form.errors, err_key='validate_err')

        account_id       = g.account_id
        title            = self.request.json['title']
        summary          = self.request.json['summary']
        content_type     = self.request.json['content_type']
        content          = self.request.json['content']
        content_markdown = self.request.json['content_markdown']
        # TODO: word_count 计算
        word_count  = 0
        category_id = self.request.json['category_id']
        tags        = self.request.json['tags']
        status      = self.request.json['status'] if 'status' in self.request.json else ArticleModel.status_draft

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


