'''
@Descripttion: 公共类，提供常用方法
@version: v1.0
@Author: JalanJiang
@Date: 2019-06-03 23:19:33
@LastEditTime: 2019-06-04 00:40:56
'''
from flask import jsonify
import json

class Base():
    def return_json(self, body={}):
        '''
        @descripttion: 返回 JSON 数据
        @param dict body 数据主体
        @return: JSON 结果
        '''
        return jsonify(body)

    def return_error(self, err_code, err_msg=''):
        '''
        @descripttion: 返回错误数据
        @param integer err_code 错误码
        @param string  err_msg  错误信息
        @return: JSON 结果
        '''
        return self.return_json({
            'err_code': err_code,
            'err_msg': err_msg
        })

    def return_success(self, data={}):
        '''
        @descripttion: 返回正确结果数据
        @param dict data 数据主体
        @return: JSON 结果
        '''
        # return data
        return self.return_json(data)