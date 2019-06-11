'''
@Description: 站点配置
@Version: v1.0
@Author: JalanJiang
@Date: 2019-06-06 15:37:17
@LastEditTime: 2019-06-11 23:24:57
'''

role_ids = [10, 20]

roles = [
    {
        'id': 10,
        'name': '超级管理员'
    },
    {
        'id': 20,
        'name': '文章管理员'
    }
]

role_menus = {
    10: ['article', 'site', 'account', 'dashboard'],
    20: ['article']
}

menus = {
    'article': {
        'name': 'article',
        'title': '文章管理',
        'path': '/articles',
        'icon': '',
        'children': [
            {
                'name': 'article_list',
                'path': '',
                'title': '文章列表'
            }
        ]
    },
    'account': {
        'name': 'account',
        'title': '账号管理',
        'path': '/accounts',
        'icon': '',
    },
    'dashboard': {
        "icon": "",
        "name": "dashboard",
        "path": "/dashboard",
        "title": "仪表盘"
    },
    'site': {
        'name': 'site',
        'title': '站点管理',
        'path': '/sites',
        'icon': '',
    }
}