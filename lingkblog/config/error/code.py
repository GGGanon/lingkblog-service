'''
@Description: 错误码定义（http 状态码 + 模块 + 错误类型）
@Version: v1.0
@Author: JalanJiang
@Date: 2019-06-06 12:37:42
@LastEditTime: 2019-06-30 00:05:46
'''

error_code = {
    'validate_err': 10000,
    # 授权相关
    'login_fail': 10001, # 登录失败
    'invalid_token': 10002,
    'expired_token': 10006,

    # user模块 - 11
    'account_not_found': 11001,
    # account模块 - 12
    'email_already_exist': 12001,
    # article 模块 - 13
    'article_not_found': 13001,

    # site 模块 - 14
    'site_article_category_exist': 14001,
    'site_config_not_found': 14002,

    # 系统拦截错误
    'system_err': 50000,
}