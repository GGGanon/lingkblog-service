'''
@Descripttion: 初始化
@version: v1.0
@Author: JalanJiang
@Date: 2019-06-02 14:07:48
@LastEditTime: 2019-06-05 14:18:19
'''
from flask import Flask, g
from flask_sqlalchemy import SQLAlchemy


def create_app(test_config=None):
    '''
    @descripttion: 初始化工厂
    @param {type} 
    @return: Flask 实例
    '''
    # 创建一个 Flask 实例
    app = Flask(__name__, instance_relative_config=True)

    # test
    # @app.route("/hello")
    # def hello():
    #     return "Hello, LingKBlog!"

    # 路由注册
    from lingkblog.routes.admin import user
    from lingkblog.routes.admin import account
    app.register_blueprint(user.bp)
    app.register_blueprint(account.bp)

    # 加载配置文件
    app.config.from_object('config')

    return app