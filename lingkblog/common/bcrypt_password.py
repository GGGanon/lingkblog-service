'''
@Description: 密码加密工具
@Version: v1.0
@Author: JalanJiang
@Date: 2019-06-06 09:44:33
@LastEditTime: 2019-06-06 15:02:33
'''
import bcrypt


class BcryptPassword():

    @staticmethod
    def encode_password(password):
        '''
        @description: 密码加密
        @param : string password 待加密密码
        @return: string 加密结果
        '''
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hashed

    @staticmethod
    def check_password(input_password, db_password):
        '''
        @description: 验证密码正确性
        @param : string input_password 用户输入的密码
        @param : string db_password 数据库存在的密码
        @return: 验证成功返回 True，否则返回 False
        '''
        if bcrypt.hashpw(input_password.encode('utf-8'), db_password) == db_password:
            return True
        else:
            return False
