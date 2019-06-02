'''
@Descripttion: 登录验证中间件
@version: v1.0
@Author: JalanJiang
@Date: 2019-06-03 00:13:35
@LastEditTime: 2019-06-03 00:19:07
'''

class auth_middleware():
    def __init__(self, wsgi_app):
        self.wsgi_app = wsgi_app

    def __call__(self, *args, **kwargs):
        print('before')
        res = self.wsgi_app(*args, **kwargs)
        print('after')å
        return res