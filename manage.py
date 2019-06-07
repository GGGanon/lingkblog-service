'''
@Description: Migrate 管理
@Version: v1.0
@Author: JalanJiang
@Date: 2019-06-05 14:40:45
@LastEditTime: 2019-06-07 12:40:40
'''
from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from lingkblog import db
from app import app

# 导入相关模型
from lingkblog.models.account import Account
from lingkblog.models.article import Article
from lingkblog.models.operation import Operation
from lingkblog.models.visit import Visit

# app = Flask(__name__)
# app.config.from_object('config')
# db = SQLAlchemy(app)

manager = Manager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()