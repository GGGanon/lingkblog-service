'''
@Descripttion: 公共类，提供常用方法
@version: v1.0
@Author: JalanJiang
@Date: 2019-06-03 23:19:33
@LastEditTime: 2019-06-16 01:47:01
'''
from flask import jsonify, Response
from lingkblog import app
import json
import time


class Base():


    def __init__(self, request):
        self.request = request
    
    def return_json(self, body={}):
        '''
        @descripttion: 返回 JSON 数据
        @param dict body 数据主体
        @return: JSON 结果
        '''
        if body:
            return jsonify(body)
        else:
            return ('')

    def return_error(self, http_status_code, err_code=0, err_msg=''):
        '''
        @descripttion: 返回错误数据（暂时无用）
        @param integer http_status_code HTTP状态码
        @param integer err_code 错误码
        @param string  err_msg  错误信息
        @return: JSON 结果
        '''
        if (err_code == 0):
            err_code = http_status_code
        
        response_data = self.return_json({
            'err_code': err_code,
            'err_msg' : err_msg
        })

        return response_data, 400

    def return_success(self, data={}):
        '''
        @descripttion: 返回正确结果数据
        @param dict data 数据主体
        @return: JSON 结果
        '''
        # return data
        return self.return_json(data)

    def datetime_to_timestamp(self, datetime):
        '''
        @descripttion: datetime 转 UNIX 时间戳
        @param datetime datetime 时间
        @return: UNIX 时间戳
        '''
        return time.mktime(datetime.timetuple())