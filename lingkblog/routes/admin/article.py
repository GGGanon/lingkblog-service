'''
@Descripttion: 文章管理路由
@version: v1.0
@Author: JalanJiang
@Date: 2019-06-07 21:42:59
@LastEditTime: 2019-06-18 16:55:03
'''
from flask import Blueprint, request
from lingkblog.services.admin.article import Article as ArticleService


bp = Blueprint('article', __name__, url_prefix='/admin-api/articles')

@bp.route('', methods=['GET'])
def get_articles():
    article = ArticleService(request)
    return article.index()

@bp.route('/<int:id>', methods=['GET'])
def get_article(id):
    article = ArticleService(request)
    return article.show(id)

@bp.route('', methods=['POST'])
def add_article():
    article = ArticleService(request)
    return article.store()

@bp.route('/<int:id>', methods=['PUT'])
def update_article(id):
    article = ArticleService(request)
    return article.update(id)

@bp.route('/<int:id>', methods=['PATCH'])
def update_part_article(id):
    article = ArticleService(request)
    return article.partical_update(id)

@bp.route('/<int:id>', methods=['DELETE'])
def delete_article(id):
    article = ArticleService(request)
    return article.delete(id)