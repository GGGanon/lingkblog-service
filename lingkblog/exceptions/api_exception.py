'''
@Description: API 异常捕获
@Version: v1.0
@Author: JalanJiang
@Date: 2019-06-06 10:42:35
@LastEditTime: 2019-06-06 11:21:01
'''
class APIException(Exception):
    def __init__(self, status_code=400, err_code=0, err_msg=''):
        super().__init__()
        self.status_code = status_code
        self.err_code = err_code
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