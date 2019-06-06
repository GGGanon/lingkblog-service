'''
@Descripttion: 
@version: v1.0
@Author: JalanJiang
@Date: 2019-06-03 23:03:33
@LastEditTime: 2019-06-06 14:16:22
'''
from lingkblog.common.jwt_auth import JWTAuth
from lingkblog.services.base import Base as BaseService
from lingkblog.common.validators.login_form import LoginForm
from lingkblog.common.validators.store_account_form import StoreAccountForm
from lingkblog.models.account import Account
from flask_api import status
from lingkblog import db
import time


class User(BaseService):

    def login(self):
        '''
        @descripttion: /admin-api/users/token 用户登录方法
        @param body email 用户邮箱
        @param body password 用户密码
        @return: 
        '''
        # 请求参数验证
        login_form = LoginForm(self.request.form)
        if not login_form.validate():
            return self.return_error(status.HTTP_400_BAD_REQUEST, login_form.errors)

        email    = self.request.form['email']
        password = self.request.form['password']
        
        # TODO: 暂为测试用，后续补充验证逻辑
        if email == 'yahaha@gmail.com' and password == 'test@123':
            # 登录成功
            user_id       = 1
            updated_at    = int(time.time())
            access_token  = JWTAuth.encode_access_token(user_id, updated_at)
            response_data = {
                'access_token': bytes.decode(access_token),
                'expire_at': 7200
            }
            return self.return_success(response_data)
        else:
            # 登录失败
            return self.return_error(status.HTTP_400_BAD_REQUEST, '登录失败')