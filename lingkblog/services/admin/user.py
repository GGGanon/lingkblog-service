'''
@Descripttion: 
@version: v1.0
@Author: JalanJiang
@Date: 2019-06-03 23:03:33
@LastEditTime: 2019-06-06 14:58:46
'''
from lingkblog.common.jwt_auth import JWTAuth
from lingkblog.common.validators.login_form import LoginForm
from lingkblog.common.validators.store_account_form import StoreAccountForm
from lingkblog.common.bcrypt_password import BcryptPassword
from lingkblog.services.base import Base as BaseService
from lingkblog.models.account import Account as AccountModel
from lingkblog.exceptions.api_exception import APIException
from lingkblog import db

from flask_api import status
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
            raise APIException(err_key='validate_err', err_msg=login_form.errors)

        email    = self.request.form['email']
        password = self.request.form['password']

        # 判断用户是否存在
        account_obj = AccountModel.query.filter_by(email=email).first()
        if account_obj is None:
            # 用户不存在
            raise APIException(err_key='account_not_found')

        account_id = account_obj.id
        account_password = account_obj.password

        # 密码校验
        if BcryptPassword.check_password(password, account_password):
            # 登录成功
            updated_at    = int(time.time())
            access_token  = JWTAuth.encode_access_token(account_id, updated_at)
            response_data = {
                # TODO：refreshToken 功能
                'refresh_token': '',
                'token_type': 'bearer',
                'access_token': bytes.decode(access_token),
                'expires_in': 7200
            }
            return self.return_success(response_data)
            
        else:
            # 登录失败
            raise APIException(err_key='login_fail')