from flask import Flask, request
from json_response import JsonResponse
from database.database import db
import json
from log.logger import log_route

def login_route(app: Flask):
    @app.route("/login", methods=["POST"])
    @log_route
    def login():
        data = json.loads(request.data)  # 将json字符串转为dict
        print(f'reques:{data}')
        result = db.execute(sql='select password, identity from login where username = %s', args=[data['username']])
        print(result)
        if len(result) == 0:
            ok2login = False
        else:
            ok2login = (result[0]['password'] == data['password'])
        
        if ok2login:
            user_data = {
                'username': data['username'],
                'identity': result[0]['identity']
            }
            return JsonResponse.success(msg='登录成功', data=user_data)
        else:
            return JsonResponse.fail(msg='登录失败,请重新输入账号和密码')