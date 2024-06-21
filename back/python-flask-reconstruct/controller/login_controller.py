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
        result = db.execute(sql='select password from login where username = %s',
                            args=[data['username']])
        print(result)
        ok2login = (result[0]['password'] == data['password'])
        return JsonResponse.success(msg='登录成功', data=result) if ok2login else JsonResponse.fail(msg='登录失败,请重新输入账号和密码')