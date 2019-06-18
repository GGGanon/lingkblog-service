'''
@Description: 
@Version: v1.0
@Author: JalanJiang
@Date: 2019-06-12 16:20:20
@LastEditTime: 2019-06-19 00:23:11
'''
import datetime
from sqlalchemy.sql import and_
from flask_api import status as http_status

from lingkblog import db
from lingkblog.services.base import Base as BaseService
from lingkblog.exceptions.api_exception import APIException
from lingkblog.models.account import Account as AccountModel
from lingkblog.common.bcrypt_password import BcryptPassword
from lingkblog.common.validators.store_account_form import StoreAccountForm


class Account(BaseService):

    def index(self):
        # TODO: 请求参数验证

        # 参数初始化
        page    = int(self.request.args.get('page', 1))
        limit   = int(self.request.args.get('limit', 20))
        email   = self.request.args.get('email', '')
        name    = self.request.args.get('name', '')
        role_id = self.request.args.get('role_id', 0)
        status  = self.request.args.get('status', -1)

        # 构造查询器
        condition = list()
        if email:
            condition.append(AccountModel.email == email)
        else:
            if name:
                condition.append(AccountModel.name.like("%" + name + "%"))
            if role_id:
                condition.append(AccountModel.role_id == role_id)
            if status != -1:
                condition.append(AccountModel.status == status)
        account_pages = AccountModel.query.filter(*condition).paginate(page=page, per_page=limit)

        accounts = list()
        for account_obj in account_pages.items:
            accounts.append({
                'id'     : account_obj.id,
                'email'  : account_obj.email,
                'name'   : account_obj.name,
                'role_id': account_obj.role_id,
                'status' : account_obj.status
            })

        return self.return_success({
            'pages': account_pages.pages,
            'total': account_pages.total,
            'accounts': accounts
        })


    def store(self):
        '''
        @description: 新增账号
        @param : 
        @return: 新增账号信息
        '''
        store_account_form = StoreAccountForm.from_json(self.request.json)
        if not store_account_form.validate():
            raise APIException(err_msg=store_account_form.errors, err_key='validate_err')

        name     = self.request.json['name']
        email    = self.request.json['email']
        password = BcryptPassword.encode_password(self.request.json['password'])
        # TODO：校验合法性
        role_id  = self.request.json['role_id']
        status   = self.request.json['status']

        # 判断 email 是否已存在
        if AccountModel.query.filter_by(email=email).first():
            raise APIException(err_key='email_already_exist')

        # 新增数据库入
        account_obj = AccountModel(name=name, email=email, password=password, role_id=role_id, status=status)
        db.session.add(account_obj)
        db.session.commit()

        return self.return_success({
            'id'     : account_obj.id,
            'name'   : name,
            'email'  : email,
            'role_id': role_id,
            'status' : status
        })

    def delete(self, id):
        '''
        @descripttion: 删除账号
        @param path int id 用户ID
        @return: 空文档
        '''
        account_obj = AccountModel.query.filter_by(id=id).first()
        if not account_obj:
            raise APIException(err_key='account_not_found')
        account_obj.deleted_at = datetime.datetime.now()
        db.session.commit()
        return self.return_success()