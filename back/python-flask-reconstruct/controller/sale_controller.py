from flask import Flask, request
from json_response import JsonResponse
from database.database import db
import json
from datetime import datetime
from log.logger import log_route

def sale_route(app: Flask):
    #sale表
    @app.route("/all_sale", methods=["GET"])  # 查询（全部）
    @log_route
    def all_sale():
        result = db.execute(sql='select * from sale')
        return JsonResponse.success(msg='查询成功', data=result)

    @app.route("/add_sale", methods=["POST"])  # 添加（单个）
    @log_route
    def add_sale():
        data = json.loads(request.data)  # 将json字符串转为dict
        isOk = db.execute(sql='insert into sale(sale_id, client_id, goods_id, sale_price, sale_num, sale_amount, sale_date) values(%s,%s,%s,%s,%s,%s,%s)',
                        args=[data['sale_id'], data['client_id'], data['goods_id'], data['sale_price'], data['sale_num'], data['sale_amount'], data['sale_date']])
        # python三元表达式
        return JsonResponse.success(msg='销售表添加成功') if not isOk else JsonResponse.fail(msg='销售表添加失败')

    @app.route("/update_sale", methods=["PUT"])  # 修改（单个）
    @log_route
    def update_sale():
        # request.data获取请求体数据
        # 前端在发送请求时，由于指定了Content-Type为application/json；故request.data获取到的就是json数据
        data = json.loads(request.data)  # 将json字符串转为dict
        if 'sale_id' not in data:  # 改为form里对应的xx_id
            return JsonResponse.fail(msg='需要传入sale_id')
        sale_date = datetime.strptime(data['sale_date'], '%a, %d %b %Y %H:%M:%S %Z').strftime('%Y-%m-%d')
        isOk = db.execute(sql='update sale set client_id=%s,goods_id=%s,sale_price=%s,sale_num=%s,sale_amount=%s,sale_date=%s where sale_id=%s',  # 改为
                        args=[data['client_id'], data['goods_id'], data['sale_price'], data['sale_num'], data['sale_amount'], sale_date, data['sale_id']])
        return JsonResponse.success(msg='修改成功') if not isOk else JsonResponse.fail(msg='修改失败')
