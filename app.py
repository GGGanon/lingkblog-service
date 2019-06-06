'''
@Descripttion: 应用入口
@version: v1.0
@Author: JalanJiang
@Date: 2019-06-02 01:43:27
@LastEditTime: 2019-06-06 18:41:46
'''
from lingkblog import create_app
from lingkblog.common.jwt_auth import JWTAuth
from lingkblog.exceptions.api_exception import APIException
from lingkblog.models.account import Account as AccountModel

from flask_sqlalchemy import SQLAlchemy
# from config import DATABASE
from flask import g, request
import sqlite3


app = create_app()

@app.before_request
def check_auth_token():
    special_route = ['/admin-api/users/token']
    if request.path not in special_route:
        access_token = request.headers.get('Authorization')
        payload      = JWTAuth.decode_access_token(access_token)
        account_id   = payload['data']['id']

        # 判断用户是否存在
        account_obj = AccountModel.query.filter_by(id=account_id).first()
        if account_obj is None:
            raise APIException(err_key='invalid_token')

        g.account_id  = account_id
        g.account_obj = account_obj

        
if __name__ == "__main__":
    app.run()