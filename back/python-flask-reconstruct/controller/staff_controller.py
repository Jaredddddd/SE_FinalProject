from flask import Flask, request
from json_response import JsonResponse
from database.database import db
import json
from log.logger import log_route

def staff_route(app: Flask):
    # staff表
    @app.route("/all_staff", methods=["GET"])  # 查询（全部）
    @log_route
    def all_staff():
        result = db.execute(sql='select * from staff')
        return JsonResponse.success(msg='查询成功', data=result)

    @app.route("/add_staff", methods=["POST"])  # 添加（单个）
    @log_route
    def add_staff():
        data = json.loads(request.data)  # 将json字符串转为dict
        isOk = db.execute(sql='insert into staff(staff_id,staff_name,department,salary,phone_number) values(%s,%s,%s,%s,%s)',
                        args=[data['staff_id'], data['staff_name'], data['department'], data['salary'],  data['phone_number']])
        # python三元表达式
        return JsonResponse.success(msg='添加成功') if not isOk else JsonResponse.fail(msg='添加失败')

    @app.route("/update_staff", methods=["PUT"])  # 修改（单个）
    @log_route
    def update_staff():
        # request.data获取请求体数据
        # 前端在发送请求时，由于指定了Content-Type为application/json；故request.data获取到的就是json数据
        data = json.loads(request.data)  # 将json字符串转为dict
        if 'staff_id' not in data:  # 改为form里对应的xx_id
            return JsonResponse.fail(msg='需要传入staff_id')
        isOk = db.execute(sql='update staff set staff_name=%s,department=%s,salary=%s,phone_number=%s where staff_id=%s',  # 改为
                        args=[data['staff_name'], data['department'], data['salary'], data['phone_number'], data['staff_id']])
        return JsonResponse.success(msg='修改成功') if not isOk else JsonResponse.fail(msg='修改失败')


    @app.route("/delete_staff", methods=["DELETE"])  # 删除（单个）
    @log_route
    def delete_staff():
        # request.args获取请求链接中 ? 后面的所有参数；以字典的方式存储
        if 'staff_id' not in request.args:
            return JsonResponse.fail(msg='需要传入staff_id')
        isOk = db.execute(sql='delete from staff where staff_id=%s', args=[request.args['staff_id']])
        return JsonResponse.success(msg='删除成功') if not isOk else JsonResponse.fail(msg='删除失败')

