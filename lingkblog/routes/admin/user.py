'''
@Descripttion: 管理后台当前用户相关路由
@version: v1.0
@Author: JalanJiang
@Date: 2019-06-02 15:08:20
@LastEditTime: 2019-06-04 00:24:49
'''
from flask import Blueprint, request
from lingkblog.services.user import User as UserService

bp = Blueprint("token", __name__, url_prefix="/admin-api/users")


@bp.route("/token", methods=['POST', 'GET', 'DELETE'])
def account_token():
    if request.method == 'POST':
        user = UserService(request)
        return user.login()
        # pass
    if request.method == 'PUT':
        pass
    if request.method == 'DELETE':
        pass
    # return "Hello, LingKBlog Users!"