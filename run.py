'''
@Descripttion: 应用入口
@version: v1.0
@Author: JalanJiang
@Date: 2019-06-02 01:43:27
@LastEditTime: 2019-06-02 15:46:00
'''
from lingkblog import create_app

app = create_app()
app.run()