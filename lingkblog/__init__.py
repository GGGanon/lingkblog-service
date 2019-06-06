'''
@Descripttion: 初始化
@version: v1.0
@Author: JalanJiang
@Date: 2019-06-02 14:07:48
@LastEditTime: 2019-06-06 11:24:04
'''
from flask import Flask, g, jsonify
from flask_sqlalchemy import SQLAlchemy
from lingkblog.exceptions.api_exception import APIException

db = SQLAlchemy()
# 创建一个 Flask 实例
app = Flask(__name__, instance_relative_config=True)

def create_app(test_config=None):
    '''
    @descripttion: 初始化工厂
    @param {type} 
    @return: Flask 实例
    '''
    # app = Flask(__name__, instance_relative_config=True)
    db.init_app(app)

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

@app.errorhandler(APIException)
def handle_api_exception(error):
    '''
    @description: 错误统一处理方法
    @param : error 异常
    @return: resposne 返回值
    '''
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response