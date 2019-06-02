'''
@Descripttion: 管理后台账号相关路由
@version: v1.0
@Author: JalanJiang
@Date: 2019-06-02 15:25:56
@LastEditTime: 2019-06-02 15:44:23
'''
from flask import Blueprint


bp = Blueprint('account', __name__, url_prefix='/admin-api/accounts')


@bp.route('', methods=['POST', 'GET', 'DELETE', 'PUT'])
def handle_accounts():
    '''
    @descripttion: 账号相关操作
    @param {type} 
    @return: 
    '''
    return "Hello, LingKBlog Account!"