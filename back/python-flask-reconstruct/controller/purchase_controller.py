from flask import Flask, request
from json_response import JsonResponse
from database.database import db
import json
from datetime import datetime
from log.logger import log_route

def purchase_route(app: Flask):
    # purchase表
    @app.route("/all_purchase", methods=["GET"])  # 查询（全部）
    @log_route
    def all_purchase():
        result = db.get_list(sql='select * from purchase')
        return JsonResponse.success(msg='查询成功', data=result)


    @app.route("/add_purchase", methods=["POST"])  # 添加（单个）
    @ log_route
    def add_purchase():
        data = json.loads(request.data)  # 将json字符串转为dict
        isOk = db.modify(sql='insert into purchase(purchase_id,staff_id,goods_id,purchase_price,purchase_num,purchase_amount,purchase_date) values(%s,%s,%s,%s,%s,%s,%s)',
                        args=[data['purchase_id'], data['staff_id'], data['goods_id'], data['purchase_price'], data['purchase_num'], data['purchase_amount'], data['purchase_date']])
        # python三元表达式
        return JsonResponse.success(msg='添加成功') if isOk else JsonResponse.fail(msg='添加失败')


    @app.route("/update_purchase", methods=["PUT"])  # 修改（单个）
    @log_route
    def update_purchase():
        # request.data获取请求体数据
        # 前端在发送请求时，由于指定了Content-Type为application/json；故request.data获取到的就是json数据
        data = json.loads(request.data)  # 将json字符串转为dict
        if 'purchase_id' not in data:  # 改为form里对应的xx_id
            return JsonResponse.fail(msg='需要传入purchase_id')
        sale_date = datetime.strptime(data['sale_date'], '%a, %d %b %Y %H:%M:%S %Z').strftime('%Y-%m-%d')
        isOk = db.modify(sql='update purchase set staff_id=%s, goods_id=%s, purchase_price=%s, purchase_num=%s, purchase_amount=%s, purchase_date=%s  where purchase_id=%s',  # 改为
                        args=[data['staff_id'], data['goods_id'], data['purchase_price'], data['purchase_num'], data['purchase_amount'], sale_date])
        return JsonResponse.success(msg='修改成功') if isOk else JsonResponse.fail(msg='商品编号不可修改')


    @app.route("/delete_purchase", methods=["DELETE"])  # 删除（单个）
    @log_route
    def delete_purchase():
        # request.args获取请求链接中 ? 后面的所有参数；以字典的方式存储
        if 'purchase_id' not in request.args:
            return JsonResponse.fail(msg='需要传入purchase_id')
        isOk = db.modify(sql='delete from purchase where purchase_id=%s', args=[request.args['purchase_id']])
        return JsonResponse.success(msg='删除成功') if isOk else JsonResponse.fail(msg='删除失败')
