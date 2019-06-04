'''
@Descripttion: 用户登录表单验证器
@version: v1.0
@Author: JalanJiang
@Date: 2019-06-05 00:52:02
@LastEditTime: 2019-06-05 01:15:40
'''
from wtforms import Form, StringField, TextField
from wtforms.validators import Email, input_required


class LoginForm(Form):
    email = StringField(validators=[Email(), input_required()])
    # TODO：密码长度限制
    password = StringField(validators=[input_required()])