from lingkblog.services.base import Base as BaseService
from lingkblog.common.validators.store_account_form import StoreAccountForm
from lingkblog.models.account import Account as AccountModel
from lingkblog import db
from lingkblog.common.bcrypt_password import BcryptPassword
from lingkblog.exceptions.api_exception import APIException

from flask_api import status as http_status


class Account(BaseService):

    def store(self):
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