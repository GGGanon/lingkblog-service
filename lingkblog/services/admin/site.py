'''
@Description: 站点管理
@Version: v1.0
@Author: JalanJiang
@Date: 2019-06-06 15:40:11
@LastEditTime: 2019-06-12 16:18:03
'''
from lingkblog import db
from lingkblog.config import site
from lingkblog.services.base import Base
from lingkblog.models.account import Account as AccountModel
from lingkblog.models.article_category import ArticleCategory as ArticleCategoryModel
from lingkblog.exceptions.api_exception import APIException
from lingkblog.common.validators.store_article_category_form import StoreArticleCategoryForm

from flask import request, g


class Site(Base):
    
    def get_menus(self):
        '''
        @description: 获取权限菜单
        @return: list 菜单列表
        '''
        role_id = g.account_obj.role_id
        menus = list()
        if role_id in site.role_menus:
            role_menus = site.role_menus[role_id]
            for menu_name in role_menus:
                menus.append(site.menus[menu_name])
            
        return self.return_success(menus)

    def store_article_category(self):
        '''
        @descripttion: 新增文章分类
        @param {type} 
        @return: 
        '''
        # 参数验证
        store_article_category_form = StoreArticleCategoryForm.from_json(self.request.json)
        if not store_article_category_form.validate():
            raise APIException(err_msg=store_article_category_form.errors, err_key='validate_err')
        
        name = self.request.json['name']
        # 判断分类名称是否已存在
        if ArticleCategoryModel.query.filter_by(name=name).first():
            raise APIException(err_key='site_article_category_exist')

        # 新增分类入库
        article_category_obj = ArticleCategoryModel(name=name)
        db.session.add(article_category_obj)
        db.session.commit()
        
        return self.return_success({
            'id': article_category_obj.id,
            'name': name
        })
        
    def index_article_category(self):
        '''
        @descripttion: 获取文章分类列表
        @return: 
        '''
        article_category_objs = ArticleCategoryModel.query.all()
        article_category_list = list()
        for article_category_obj in article_category_objs:
            article_category_list.append({
                'id': article_category_obj.id,
                'name': article_category_obj.name,
            })
        return self.return_success(article_category_list)

    def update_article_category(self, id):
        '''
        @descripttion: 更新文章类型名称
        @param path int id 文章类型ID
        @return: 
        '''
        # 参数验证
        store_article_category_form = StoreArticleCategoryForm.from_json(self.request.json)
        if not store_article_category_form.validate():
            raise APIException(err_msg=store_article_category_form.errors, err_key='validate_err')
            
        name = self.request.json['name']
        article_category_obj = ArticleCategoryModel.query.filter_by(id=id).update({'name': name})
        db.session.commit()
        return self.return_success({
            'id': id,
            'name': name,
        })