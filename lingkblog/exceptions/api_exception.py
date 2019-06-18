'''
@Description: API 异常捕获
@Version: v1.0
@Author: JalanJiang
@Date: 2019-06-06 10:42:35
@LastEditTime: 2019-06-18 17:19:45
'''
from lingkblog.config.error.code import error_code
from lingkblog.config.error.message import error_message


class APIException(Exception):

    
    def __init__(self, err_key='validate_err', err_msg='参数有误', http_status_code=400):
        super().__init__()
        # TODO: 不存在键值处理
        self.status_code = http_status_code
        self.err_code = error_code[err_key]
        if (err_key != 'validate_err'):
            self.err_msg = error_message[self.err_code]
        else:
            self.err_msg = err_msg

    def to_dict(self):
        '''
        @description: 构造要返回的错误数据字典
        @return: dict 错误数据字典
        '''
        return {
            'err_code': self.err_code,
            'err_msg': self.err_msg
        }