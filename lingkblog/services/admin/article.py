'''
@Descripttion: 文章控制器
@version: v1.0
@Author: JalanJiang
@Date: 2019-06-07 21:43:07
@LastEditTime: 2019-06-29 23:35:44
'''
from flask import g, jsonify
from sqlalchemy.sql import and_
from flask_api import status as http_status
import json
import datetime

from lingkblog import db
from lingkblog.common.create_uuid import CreateUUID
from lingkblog.services.base import Base
from lingkblog.models.article import Article as ArticleModel
from lingkblog.exceptions.api_exception import APIException
from lingkblog.common.validators.store_article_form import StoreArticleForm
from lingkblog.exceptions.api_exception import APIException
from lingkblog.common.validators.request_articles import RequestArticles


class Article(Base):

    def index(self):
        '''
        @descripttion: 获取文章列表
        @param query int    page         页码
        @param query int    limit        每页数量
        @param query string title        文章标题
        @param query int    category_id  文章分类ID
        @param query string tags         标签（待定）
        @return: 
        '''
        # 请求参数验证
        request_articles = RequestArticles(self.request.args)
        if not request_articles.validate():
            raise APIException(err_key='validate_err', err_msg=request_articles.errors)

        page        = int(self.request.args.get('page', 1))
        limit       = int(self.request.args.get('limit', 20))
        title       = self.request.args.get('title', '')
        category_id = int(self.request.args.get('category_id', 0))

        # 构造查询
        condition = list()
        if title:
            condition.append(ArticleModel.title.like("%" + title + "%"))
        if category_id:
            condition.append(ArticleModel.category_id == category_id)
        article_pages = ArticleModel.query.filter(*condition).paginate(page=page, per_page=limit)

        articles = list()
        for article_obj in article_pages.items:
            articles.append({
                'id'         : article_obj.id,
                'uuid'       : article_obj.uuid,
                'title'      : article_obj.title,
                'summary'    : article_obj.summary,
                'created_at' : self.datetime_to_timestamp(article_obj.created_at),
                'updated_at' : self.datetime_to_timestamp(article_obj.updated_at),
                'status'     : article_obj.status,
                'category_id': article_obj.category_id,
                'tags'       : article_obj.tags
            })
            
        return self.return_success({
            'pages': article_pages.pages,
            'total': article_pages.total,
            'articles': articles
        })

    def show(self, uuid):
        '''
        @descripttion: 获取文章详情
        @param path int uuid 文章唯一标识
        @return: 
        '''
        article_obj = ArticleModel.query.filter_by(uuid=uuid).first()
        if not article_obj:
            raise APIException(err_key='article_not_found', http_status_code=http_status.HTTP_404_NOT_FOUND)
        
        return self.return_success({
            'id'              : article_obj.id,
            'uuid'            : article_obj.uuid,
            'title'           : article_obj.title,
            'content_type'    : article_obj.content_type,
            'status'          : article_obj.status,
            'word_count'      : article_obj.word_count,
            'content'         : article_obj.content,
            'content_markdown': article_obj.content_markdown,
            'summary'         : article_obj.summary,
            'tags'            : article_obj.tags,
            'read'            : article_obj.read,
            'created_at'      : self.datetime_to_timestamp(article_obj.created_at),
            'updated_at'      : self.datetime_to_timestamp(article_obj.updated_at)
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

        uuid             = CreateUUID.get_uuid() # 生成 uuid
        print(uuid)
        account_id       = g.account_id
        title            = self.request.json['title']
        summary          = self.request.json['summary']
        content_type     = self.request.json['content_type']
        content          = self.request.json['content']
        content_markdown = self.request.json['content_markdown']
        word_count       = self.request.json['word_count']
        category_id      = self.request.json['category_id']
        tags             = self.request.json['tags']
        status           = self.request.json['status'] if 'status' in self.request.json else ArticleModel.status_draft

        # 新增文章
        article_obj = ArticleModel(
            uuid=uuid,
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
            'id'              : article_obj.id,
            'uuid'            : article_obj.uuid,
            'account_id'      : article_obj.account_id,
            'title'           : article_obj.title,
            'summary'         : article_obj.summary,
            'content_type'    : article_obj.content_type,
            'content'         : article_obj.content,
            'content_markdown': article_obj.content_markdown,
            'word_count'      : article_obj.word_count,
            'read'            : article_obj.read,
            'category_id'     : article_obj.category_id,
            'tags'            : article_obj.tags,
            'status'          : article_obj.status,
            'created_at'      : self.datetime_to_timestamp(article_obj.created_at),
            'updated_at'      : self.datetime_to_timestamp(article_obj.updated_at)
        })

    def update(self, uuid):
        '''
        @description: 更新文章
        @param : path int id 文章ID
        @return: 更新后的文章资源数据
        '''
        # TODO: 参数验证

        article_obj = ArticleModel.query.filter_by(uuid=uuid).first()
        if not article_obj:
            raise APIException(err_key='article_not_found', http_status_code=http_status.HTTP_404_NOT_FOUND)

        title            = self.request.json['title']
        summary          = self.request.json['summary']
        content_type     = self.request.json['content_type']
        content          = self.request.json['content']
        content_markdown = self.request.json['content_markdown']
        word_count       = self.request.json['word_count']
        category_id      = self.request.json['category_id']
        tags             = self.request.json['tags']
        status           = self.request.json['status'] if 'status' in self.request.json else ArticleModel.status_draft
        # TODO: 是否增加更新人 updated_user

        article_obj.title = title
        article_obj.summary = summary
        article_obj.content_type = content_type
        article_obj.content = content
        article_obj.content_markdown = content_markdown
        article_obj.word_count = word_count
        article_obj.category_id = category_id
        article_obj.tags = tags
        article_obj.status = status
        db.session.commit()

        return self.return_success({
            'id'              : article_obj.id,
            'uuid'            : article_obj.uuid,
            'title'           : article_obj.title,
            'summary'         : article_obj.summary,
            'content_type'    : article_obj.content_type,
            'content'         : article_obj.content,
            'content_markdown': article_obj.content_markdown,
            'word_count'      : article_obj.word_count,
            'category_id'     : article_obj.category_id,
            'tags'            : article_obj.tags,
            'status'          : article_obj.status,
            'created_at'      : self.datetime_to_timestamp(article_obj.created_at),
            'updated_at'      : self.datetime_to_timestamp(article_obj.updated_at)
        })

    def partical_update(self, uuid):
        '''
        @description: 更新文章部分字段
        @param path int uuid 文章唯一标识
        @return: 更新后完整的文章资源对象
        '''
        # body 验证
        request_json = self.request.json
        if not request_json:
            raise APIException()

        # 判断文章ID是否存在
        article_obj = ArticleModel.query.filter_by(uuid=uuid).first()
        if not article_obj:
            raise APIException(err_key='article_not_found', http_status_code=http_status.HTTP_404_NOT_FOUND)
        
        if 'title' in request_json:
            article_obj.title = request_json['title']
        if 'summary' in request_json:
            article_obj.summary = request_json['summary']
        if 'content_type' in request_json:
            article_obj.content_type = request_json['content_type']
        if 'content' in request_json:
            article_obj.content = request_json['content']
        if 'content_markdown' in request_json:
            article_obj.content_markdown = request_json['content_markdown']
        if 'word_count' in request_json:
            article_obj.word_count = request_json['word_count']
        if 'category_id' in request_json:
            article_obj.category_id = request_json['category_id']
        if 'tags' in request_json:
            article_obj.tags = request_json['tags']
        if 'status' in request_json:
            article_obj.status = request_json['status']

        db.session.commit()

        return self.return_success({
            'id'              : article_obj.id,
            'uuid'            : article_obj.uuid,
            'title'           : article_obj.title,
            'summary'         : article_obj.summary,
            'content_type'    : article_obj.content_type,
            'content'         : article_obj.content,
            'content_markdown': article_obj.content_markdown,
            'word_count'      : article_obj.word_count,
            'category_id'     : article_obj.category_id,
            'tags'            : article_obj.tags,
            'status'          : article_obj.status,
            'created_at'      : self.datetime_to_timestamp(article_obj.created_at),
            'updated_at'      : self.datetime_to_timestamp(article_obj.updated_at)
        })

    def delete(self, uuid):
        '''
        @descripttion: 删除文章
        @param path int uuid 文章唯一标识
        @return: 
        '''
        article_obj = ArticleModel.query.filter_by(uuid=uuid).first()
        if not article_obj:
            # 文章不存在
            raise APIException(err_key='article_not_found', http_status_code=http_status.HTTP_404_NOT_FOUND)
        article_obj.deleted_at = datetime.datetime.now()
        db.session.commit()
        return self.return_success()


