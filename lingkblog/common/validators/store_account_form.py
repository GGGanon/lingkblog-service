'''
@Descripttion: 新增用户表单验证器
@version: v1.0
@Author: JalanJiang
@Date: 2019-06-05 23:02:07
@LastEditTime: 2019-06-06 01:01:45
'''
from wtforms import Form, StringField, IntegerField
from wtforms.validators import input_required, Email


class StoreAccountForm(Form):
    name = StringField(validators=[input_required()])
    email = StringField(validators=[Email(), input_required()])
    # TODO: 密码长度限制
    password = StringField(validators=[input_required()])
    role_id = IntegerField(validators=[input_required()])
    # TODO: 限制 0 或 1
    status = IntegerField(validators=[input_required()])