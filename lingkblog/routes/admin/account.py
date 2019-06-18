'''
@Descripttion: 管理后台账号相关路由
@version: v1.0
@Author: JalanJiang
@Date: 2019-06-02 15:25:56
@LastEditTime: 2019-06-19 00:34:23
'''
from flask import Blueprint, request
from lingkblog.services.admin.account import Account as AccountService


bp = Blueprint('account', __name__, url_prefix='/admin-api/accounts')


@bp.route('', methods=['GET'])
def get_accounts():
    '''
    @description: 获取账号列表
    @param : 
    @return: 账号列表
    '''
    account_service = AccountService(request)
    return account_service.index()

@bp.route('/<int:id>', methods=['GET'])
def get_account(id):
    '''
    @description: 获取指定账号信息
    @param : 
    @return: 
    '''
    pass

@bp.route('', methods=['POST'])
def add_account():
    '''
    @description: 注册新用户
    @param : 
    @return: 新注册用户资料
    '''
    account_service = AccountService(request)
    return account_service.store()

# @bp.route('/<int:id>', methods=['PUT'])
# def update_account(id):
#     '''
#     @description: 修改账号资料
#     @param : 
#     @return: 
#     '''
#     pass

@bp.route('/<int:id>', methods=['PATCH'])
def update_part_account(id):
    '''
    @description: 修改账号部分资料
    @param : 
    @return: 
    '''
    account_service = AccountService(request)
    return account_service.partical_update(id)

@bp.route('/<int:id>', methods=['DELETE'])
def delete_account(id):
    '''
    @description: 删除账号
    @param : 
    @return: 
    '''
    account_service = AccountService(request)
    return account_service.delete(id)