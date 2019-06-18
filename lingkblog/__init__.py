'''
@Descripttion: 初始化
@version: v1.0
@Author: JalanJiang
@Date: 2019-06-02 14:07:48
@LastEditTime: 2019-06-18 17:57:20
'''
import wtforms_json
from flask import Flask, g, jsonify
from flask_sqlalchemy import SQLAlchemy

from lingkblog.config.error.code import error_code
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
    wtforms_json.init()

    # test
    # @app.route("/hello")
    # def hello():
    #     return "Hello, LingKBlog!"

    # 路由注册
    from lingkblog.routes.admin import user
    from lingkblog.routes.admin import account
    from lingkblog.routes.admin import site
    from lingkblog.routes.admin import article
    app.register_blueprint(user.bp)
    app.register_blueprint(account.bp)
    app.register_blueprint(site.bp)
    app.register_blueprint(article.bp)

    # 加载配置文件
    app.config.from_object('config')

    # 加载权限验证中间件
    # app.wsgi_app = AuthMiddleware(app)

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

@app.errorhandler(Exception)
def framework_error(error):
    '''
    @description: 捕获全局异常
    @param : 异常
    @return: APIException
    '''
    if isinstance(error, APIException):
        # 如果是 APIException 异常，不做处理直接抛出
        return error
    else:
        if not app.config['DEBUG']:
            # 系统级别的异常进行封装
            code = error_code['system_err']
            msg = '未知错误'
            if hasattr(error, 'description'):
                msg = error.description
            response = jsonify({
                'err_code': code,
                'err_msg': msg
            })
            if hasattr(error, 'code'):
                response.status_code = error.code
            else:
                response.status_code = 400
            return response
        else:
            raise error
        