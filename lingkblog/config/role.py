'''
@Description: 用户角色
@Version: v1.0
@Author: JalanJiang
@Date: 2019-06-06 15:20:50
@LastEditTime: 2019-06-06 15:34:01
'''


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
    10: ['article', 'site', 'account'],
    20: ['article']
}