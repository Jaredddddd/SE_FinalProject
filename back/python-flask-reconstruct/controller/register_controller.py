'''
Author：Jared
Date：2024年06月21日
'''

from flask import Flask, request
from json_response import JsonResponse
from database.database import db
import json
from log.logger import log_route
import bcrypt


def register_route(app: Flask):
    @app.route("/register", methods=["POST"])
    @log_route
    def register():
        data = json.loads(request.data)  # 将json字符串转为dict
        print(f'request: {data}')
        if data['username'] == '':
            return JsonResponse.fail(msg='用户名不能为空')
        # 检查用户名是否已经存在
        result = db.execute(sql='select username from login where username = %s', args=[data['username']])
        if result:
            return JsonResponse.fail(msg='用户名已存在，请选择其他用户名')


        # 密码加密
        hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())

        # 插入新用户数据
        result=db.execute(sql='insert into login (username, password) values (%s, %s)',
                   args=[data['username'], hashed_password.decode('utf-8')])
        if not result:
            print(result)
            return JsonResponse.fail(msg='注册失败，请重试')
        return JsonResponse.success(msg='注册成功')


