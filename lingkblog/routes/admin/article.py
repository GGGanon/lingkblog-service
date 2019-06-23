'''
@Descripttion: 文章管理路由
@version: v1.0
@Author: JalanJiang
@Date: 2019-06-07 21:42:59
@LastEditTime: 2019-06-23 23:15:18
'''
from flask import Blueprint, request
from lingkblog.services.admin.article import Article as ArticleService


bp = Blueprint('article', __name__, url_prefix='/admin-api/articles')

@bp.route('', methods=['GET'])
def get_articles():
    article = ArticleService(request)
    return article.index()

@bp.route('/<path:uuid>', methods=['GET'])
def get_article(uuid):
    article = ArticleService(request)
    return article.show(uuid)

@bp.route('', methods=['POST'])
def add_article():
    article = ArticleService(request)
    return article.store()

@bp.route('/<path:uuid>', methods=['PUT'])
def update_article(uuid):
    article = ArticleService(request)
    return article.update(uuid)

@bp.route('/<path:uuid>', methods=['PATCH'])
def update_part_article(uuid):
    article = ArticleService(request)
    return article.partical_update(uuid)

@bp.route('/<path:uuid>', methods=['DELETE'])
def delete_article(uuid):
    article = ArticleService(request)
    return article.delete(uuid)