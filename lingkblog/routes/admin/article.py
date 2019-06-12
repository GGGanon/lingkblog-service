'''
@Descripttion: 文章管理路由
@version: v1.0
@Author: JalanJiang
@Date: 2019-06-07 21:42:59
@LastEditTime: 2019-06-12 15:18:28
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
def update_article():
    article = ArticleService(request)
    return 
    # return article.update()

@bp.route('/<int:id>', methods=['DELETE'])
def delete_article():
    return