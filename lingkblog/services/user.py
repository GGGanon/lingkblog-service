from lingkblog.common.jwt_auth import JWTAuth
from lingkblog.services.base import Base as BaseService
import time


class User(BaseService):
    def __init__(self, request):
        super().__init__()
        self.request = request

    def login(self):
        username = self.request.form['username']
        password = self.request.form['password']

        # todo: 连接数据表验证
        
        # 暂为测试用
        if username == 'admin' and password == 'admin':
            user_id = 1
            updated_at = int(time.time())
            access_token = JWTAuth.encode_access_token(user_id, updated_at)
            response_data = {
                'access_token': bytes.decode(access_token),
                'expire_at': 7200
            }
            return self.return_success(response_data)
            

