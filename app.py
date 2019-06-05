'''
@Descripttion: 应用入口
@version: v1.0
@Author: JalanJiang
@Date: 2019-06-02 01:43:27
@LastEditTime: 2019-06-06 00:26:56
'''
from lingkblog import create_app
from lingkblog.middleware import auth
from flask_sqlalchemy import SQLAlchemy
# from config import DATABASE
from flask import g
import sqlite3


# g.db = SQLAlchemy(app)

# def connect_db():
#     '''
#     @description: 连接 SQLite
#     '''
#     return sqlite3.connect(DATABASE)

# @app.before_request
# def before_request():
#     '''
#     @description: 请求前连接数据库
#     '''
#     g.db = SQLAlchemy(app)
    

# @app.teardown_request
# def teardown_request(exception):
#     '''
#     @description: 请求结束后关闭数据库连接
#     '''
#     if hasattr(g.db, 'db'):
#         g.db.close()

app = create_app()

if __name__ == "__main__":
    app.run()