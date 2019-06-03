'''
@Descripttion: 应用入口
@version: v1.0
@Author: JalanJiang
@Date: 2019-06-02 01:43:27
@LastEditTime: 2019-06-03 23:25:53
'''
from lingkblog import create_app
from lingkblog.middleware import auth


app = create_app()
app.wsgi_app = auth.AuthMiddleware(app.wsgi_app)
app.run()