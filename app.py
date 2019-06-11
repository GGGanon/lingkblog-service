'''
@Descripttion: 应用入口
@version: v1.0
@Author: JalanJiang
@Date: 2019-06-02 01:43:27
@LastEditTime: 2019-06-11 22:27:31
'''
from lingkblog import create_app
from lingkblog.common.jwt_auth import JWTAuth
from lingkblog.exceptions.api_exception import APIException
from lingkblog.models.account import Account as AccountModel

from flask_sqlalchemy import SQLAlchemy
# from config import DATABASE
from flask import g, request, make_response
import sqlite3


app = create_app()

# @app.before_request
# def check_auth_token():
#     special_route = ['/admin-api/users/token']
#     if request.path not in special_route:
#         access_token = request.headers.get('Authorization')
#         payload      = JWTAuth.decode_access_token(access_token)
#         account_id   = payload['data']['id']

#         # 判断用户是否存在
#         account_obj = AccountModel.query.filter_by(id=account_id).first()
#         if account_obj is None:
#             raise APIException(err_key='invalid_token')

#         g.account_id  = account_id
#         g.account_obj = account_obj

@app.after_request
def open_cors(response):
    '''
    @descripttion: 开启跨域调试
    @param {type} response
    @return: response
    '''
    # TODO: 区分正式与测试环境
    response = make_response(response)
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'GET,POST,PATCH,PUT,DELETE,OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type,Authorization'
    return response
        
if __name__ == "__main__":
    app.run()