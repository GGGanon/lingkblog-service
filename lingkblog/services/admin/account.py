from lingkblog.services.base import Base as BaseService
from lingkblog.common.validators.store_account_form import StoreAccountForm
from lingkblog.models.account import Account as AccountModel
from lingkblog import db
from lingkblog.common.bcrypt_password import BcryptPassword

from flask_api import status as http_status


class Account(BaseService):
    def store(self):
        store_account_form = StoreAccountForm(self.request.form)
        if store_account_form.validate() == False:
            return self.return_error(http_status.HTTP_400_BAD_REQUEST, store_account_form.errors)

        name     = self.request.form['name']
        email    = self.request.form['email']
        # TODO: 密码加密
        password = BcryptPassword.encode_password(self.request.form['password'])
        # TODO: 强制类型转换？
        role_id = self.request.form['role_id']
        status  = self.request.form['status']

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