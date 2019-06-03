'''
@Descripttion: 应用入口
@version: v1.0
@Author: JalanJiang
@Date: 2019-06-02 01:43:27
@LastEditTime: 2019-06-04 00:04:27
'''
from lingkblog import create_app
from lingkblog.middleware import auth


app = create_app()
# 加载配置文件
app.config.from_object('config')
# app.wsgi_app = auth.AuthMiddleware(app.wsgi_app)
app.run()