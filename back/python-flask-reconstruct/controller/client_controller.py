from flask import Flask, request
from json_response import JsonResponse
from database.database import db
import json
from log.logger import log_route

def client_route(app: Flask):
    # client表
    @app.route("/all_client", methods=["GET"])  # 查询（全部）
    @log_route
    def all_client():
        result = db.execute(sql='select * from client')
        return JsonResponse.success(msg='查询成功', data=result)

    @log_route
    @app.route("/add_client", methods=["POST"])  # 添加（单个）
    @log_route
    def add_client():
        data = json.loads(request.data)  # 将json字符串转为dict
        # 添加操作成功，返回None；失败，返回异常
        isOk = db.execute(sql='insert into client(client_id,client_name,phone_number,address) values(%s,%s,%s,%s)',
                        args=[data['client_id'], data['client_name'], data['phone_number'], data['address']])
        # python三元表达式
        return JsonResponse.success(msg='添加成功') if not isOk else JsonResponse.fail(msg='添加失败')

    @log_route
    @app.route("/update_client", methods=["PUT"])  # 修改（单个）
    @log_route
    def update_client():
        # request.data获取请求体数据
        # 前端在发送请求时，由于指定了Content-Type为application/json；故request.data获取到的就是json数据
        data = json.loads(request.data)  # 将json字符串转为dict
        if 'client_id' not in data:  # 改为form里对应的xx_id
            return JsonResponse.fail(msg='需要传入client_id')
        # 添加操作成功，返回None；失败，返回异常
        isOk = db.execute(sql='update client set client_name=%s,phone_number=%s,address=%s where client_id=%s',  # 改为
                        args=[data['client_name'], data['phone_number'], data['address'], data['client_id']])
        return JsonResponse.success(msg='修改成功') if not isOk else JsonResponse.fail(msg='修改失败')

    @log_route
    @app.route("/delete_client", methods=["DELETE"])  # 删除（单个）
    @log_route
    def delete_client():
        # request.args获取请求链接中 ? 后面的所有参数；以字典的方式存储
        if 'client_id' not in request.args:
            return JsonResponse.fail(msg='需要传入client_id')
        # print('delete client')
        # 删除操作成功，返回None；失败，返回异常
        isOk = db.execute(sql='delete from client where client_id=%s', args=[request.args['client_id']])
        return JsonResponse.success(msg='删除成功') if not isOk else JsonResponse.fail(msg='删除失败')
