'''
@Descripttion: 管理后台账号相关路由
@version: v1.0
@Author: JalanJiang
@Date: 2019-06-02 15:25:56
@LastEditTime: 2019-06-06 01:00:28
'''
from flask import Blueprint, request
from lingkblog.services.admin.account import Account as AccountService


bp = Blueprint('account', __name__, url_prefix='/admin-api/accounts')


@bp.route('', methods=['POST', 'GET', 'DELETE', 'PUT'])
def handle_accounts():
    '''
    @descripttion: 账号相关操作
    @param {type} 
    @return: 
    '''
    account_service = AccountService(request)
    if request.method == 'POST':
        # 注册新用户
        return account_service.store()
    elif request.method == 'GET':
        pass
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    # return "Hello, LingKBlog Account!"