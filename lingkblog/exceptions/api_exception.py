'''
@Description: API 异常捕获
@Version: v1.0
@Author: JalanJiang
@Date: 2019-06-06 10:42:35
@LastEditTime: 2019-06-06 13:09:03
'''
from lingkblog.config.error.message import error_message
from lingkblog.config.error.code import error_code


class APIException(Exception):
    def __init__(self, err_msg, err_key, http_status_code=400,):
        super().__init__()
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