'''
@Description: 站点管理
@Version: v1.0
@Author: JalanJiang
@Date: 2019-06-06 15:40:11
@LastEditTime: 2019-06-30 00:57:32
'''
from lingkblog import db, app
from lingkblog.config import site
from lingkblog.services.base import Base
from lingkblog.models.account import Account as AccountModel
from lingkblog.models.site_config import SiteConfig as SiteConfigModel
from lingkblog.models.article_category import ArticleCategory as ArticleCategoryModel
from lingkblog.exceptions.api_exception import APIException
from lingkblog.common.validators.store_article_category_form import StoreArticleCategoryForm

from flask import request, g
from flask_api import status as http_status


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
        if ArticleCategoryModel.query.filter_by(name=name).first() is not None:
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
            'id': article_category_obj.id,
            'name': article_category_obj.name,
        })

    def get_site_config(self):
        '''
        @descripttion: 获取站点配置
        @return: 站点配置对象
        '''
        # TODO：参数验证
        
        # 配置数据 ID
        site_config_id = app.config['SITE_CONFIG_ID']
        site_config_obj = SiteConfigModel.query.filter_by(id=site_config_id).first()
        if site_config_obj is None:
            raise APIException(err_key='site_config_not_found', http_status_code=http_status.HTTP_404_NOT_FOUND)
        
        return self.return_success({
            'title'      : site_config_obj.title,
            'subtitle'   : site_config_obj.subtitle,
            'description': site_config_obj.description,
            'page_size'  : site_config_obj.page_size,
            'friends'    : site_config_obj.friends,
        })

    def update_site_config(self):
        '''
        @descripttion: 更新站点配置信息
        @param {type} 
        @return: 站点配置信息资源对象
        '''
        # 配置数据 ID
        site_config_id = app.config['SITE_CONFIG_ID']
        site_config_obj = SiteConfigModel.query.filter_by(id=site_config_id).first()
        if site_config_obj is None:
            raise APIException(err_key='site_config_not_found', http_status_code=http_status.HTTP_404_NOT_FOUND)
            
        # body 验证
        request_json = self.request.json
        if request_json is None:
            raise APIException()
        
        if 'title' in request_json:
            site_config_obj.title = request_json['title']
        if 'subtitle' in request_json:
            site_config_obj.subtitle = request_json['subtitle']
        if 'description' in request_json:
            site_config_obj.description = request_json['description']
        if 'page_size' in request_json:
            site_config_obj.page_size = request_json['page_size']
        if 'friends' in request_json:
            site_config_obj.friends = request_json['friends']

        db.session.commit()

        return self.return_success({
            'title'      : site_config_obj.title,
            'subtitle'   : site_config_obj.subtitle,
            'description': site_config_obj.description,
            'page_size'  : site_config_obj.page_size,
            'friends'    : site_config_obj.friends,
        })