'''
@Descripttion: 文章列表参数验证
@version: v1.0
@Author: JalanJiang
@Date: 2019-06-16 00:09:50
@LastEditTime: 2019-06-16 01:11:14
'''
from wtforms import Form, IntegerField, StringField
from wtforms.validators import NumberRange


class RequestArticles(Form):
    page        = IntegerField(validators=[NumberRange(min=1, message='请输入有效页码')])
    limit       = IntegerField(validators=[NumberRange(min=5, max=20, message='请输入有效限制数')])
    title       = StringField()
    category_id = IntegerField()