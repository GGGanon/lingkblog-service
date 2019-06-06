'''
@Descripttion: 新增用户表单验证器
@version: v1.0
@Author: JalanJiang
@Date: 2019-06-05 23:02:07
@LastEditTime: 2019-06-06 23:46:47
'''
from wtforms import Form, StringField, IntegerField
from wtforms.validators import input_required, Email, Length, AnyOf

from lingkblog.config.site import role_ids


class StoreAccountForm(Form):
    name = StringField(validators=[input_required(message='用户名不能为空')])
    email = StringField(validators=[Email(message='请输入有效的邮箱地址'), input_required(message='邮箱不能为空')])
    # TODO: 密码长度限制
    password = StringField(validators=[input_required(message='密码不能为空'), Length(min=8, max=15, message='密码长度必须为 8~15 位')])
    role_id = IntegerField(validators=[input_required(message='用户角色不能为空'), AnyOf(values=role_ids, message='非法角色ID')])
    # TODO: 限制 0 或 1
    status = IntegerField(validators=[input_required()])