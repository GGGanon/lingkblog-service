'''
@Descripttion: JWT 服务
@version: v1.0
@Author: JalanJiang
@Date: 2019-06-03 23:39:17
@LastEditTime: 2019-06-03 23:52:15
'''
import jwt
import datetime
from config import JWT_LEEWAY, SECRET_KEY


class JWTAuth():
    @staticmethod
    def encode_access_token(user_id, updated_at):
        '''
        @descripttion: 加密获取 access_token
        @param {type} 
        @return: 
        '''
        try:
            payload = {
                'exp':
                datetime.datetime.utcnow() +
                datetime.timedelta(seconds=JWT_LEEWAY),
                'iat':
                datetime.datetime.utcnow(),
                'iss':
                'ken',
                'data': {
                    'id': user_id,
                    'updated_at': updated_at
                }
            }
            return jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        except Exception as e:
            return e