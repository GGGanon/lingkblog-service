'''
@Description: 软删除过滤查询
@Version: v1.0
@Author: JalanJiang
@Date: 2019-06-12 17:19:48
@LastEditTime: 2019-06-12 17:48:08
'''
from flask_sqlalchemy import BaseQuery


class QueryWithSoftDelete(BaseQuery):
    
    def __new__(cls, *args, **kwargs):
        obj = super(QueryWithSoftDelete, cls).__new__(cls)
        if len(args) > 0:
            super(QueryWithSoftDelete, obj).__init__(*args, **kwargs)
            return obj.filter_by(deleted_at=None)
        return obj

    def __init__(self, *args, **kwargs):
        pass