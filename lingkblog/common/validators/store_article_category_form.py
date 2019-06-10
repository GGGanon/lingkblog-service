from wtforms import Form, StringField
from wtforms.validators import input_required


class StoreArticleCategoryForm(Form):
    name = StringField(validators=[input_required(message='分类名称不能为空')])