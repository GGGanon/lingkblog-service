'''
@Descripttion: 文章管理路由
@version: v1.0
@Author: JalanJiang
@Date: 2019-06-07 21:42:59
@LastEditTime: 2019-06-07 21:55:39
'''
from flask import Blueprint, request


bp = Blueprint('article', __name__, url_prefix='/admin-api/articles')

@bp.route('', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_articles():
    '''
    @descripttion: 文章管理相关操作
    @param {type} 
    @return: 
    '''
    if request.method == 'GET':
        return
    if request.method == 'POST':
        return
    if request.method == 'PUT':
        return
    if request.method == 'DELETE':
        return