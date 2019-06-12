'''
@Descripttion: 文章管理路由
@version: v1.0
@Author: JalanJiang
@Date: 2019-06-07 21:42:59
@LastEditTime: 2019-06-12 12:00:40
'''
from flask import Blueprint, request
from lingkblog.services.admin.article import Article as ArticleService


bp = Blueprint('article', __name__, url_prefix='/admin-api/articles')

@bp.route('', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_articles():
    '''
    @descripttion: 文章管理相关操作
    @param {type} 
    @return: 
    '''
    article = ArticleService(request)
    if request.method == 'GET':
        return
    if request.method == 'POST':
        return article.store()
    if request.method == 'PUT':
        return
    if request.method == 'DELETE':
        return