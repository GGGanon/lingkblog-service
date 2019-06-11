'''
@Description: 文章提交表单验证
@Version: v1.0
@Author: JalanJiang
@Date: 2019-06-11 10:02:24
@LastEditTime: 2019-06-11 11:04:48
'''
from wtforms import Form, StringField, IntegerField
from wtforms.validators import input_required, AnyOf


class StoreArticleForm(Form):
    title = StringField(validators=[input_required(message='文章标题不能为空')])
    summary = StringField(validators=[input_required(message='文章描述不能为空')])
    content_type = IntegerField(validators=[input_required(message='文章编辑内容类型不能为空'), AnyOf(values=[1, 2], message='非法文章编辑内容类型')])
    content = StringField()
    content_markdown = StringField()
    category_id = IntegerField()
    # TODO: tags
