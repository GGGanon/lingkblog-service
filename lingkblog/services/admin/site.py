'''
@Description: 站点管理
@Version: v1.0
@Author: JalanJiang
@Date: 2019-06-06 15:40:11
@LastEditTime: 2019-06-06 18:51:19
'''
from lingkblog.config import site
from lingkblog.services.base import Base
from lingkblog.models.account import Account as AccountModel

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
