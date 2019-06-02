'''
@Descripttion: 应用入口
@version: v1.0
@Author: JalanJiang
@Date: 2019-06-02 01:43:27
@LastEditTime: 2019-06-03 00:18:15
'''
from lingkblog import create_app
from lingkblog.middleware import auth


app = create_app()
app.wsgi_app = auth.auth_middleware(app.wsgi_app)
app.run()