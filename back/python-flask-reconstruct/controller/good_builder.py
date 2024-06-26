from flask import Flask, request
from json_response import JsonResponse
from database.database import db
import json
from log.logger import log_route

def good_route(app: Flask):
    # goods表
    @app.route("/all_goods", methods=["GET"])  # 查询（全部）
    @log_route
    def all_goods():
        result = db.execute(sql='select * from goods')
        return JsonResponse.success(msg='查询成功', data=result)


    @app.route("/add_goods", methods=["POST"])  # 添加（单个
    @log_route
    def add_goods():
        data = json.loads(request.data)  # 将json字符串转为dict
        if len(data) != 3:  
            return JsonResponse.fail(msg='需要传入完整信息')
        isOk = db.execute(sql='insert into goods(goods_id,goods_name,goods_num) values(%s,%s,%s)',
                        args=[data['goods_id'], data['goods_name'], data['goods_num']])
        # python三元表达式
        return JsonResponse.success(msg='添加成功') if not isOk else JsonResponse.fail(msg='添加失败')


    @app.route("/update_goods", methods=["PUT"])  # 修改（单个）
    @log_route

    def update_goods():
        # request.data获取请求体数据
        # 前端在发送请求时，由于指定了Content-Type为application/json；故request.data获取到的就是json数据
        data = json.loads(request.data)  # 将json字符串转为dict
        if len(data) != 5:  # 改为form里对应的xx_id
            return JsonResponse.fail(msg='需要传入完整信息')
        isOk = db.execute(sql='update goods set goods_name=%s,goods_num=%s where goods_id=%s',  # 改为
                        args=[data['goods_name'], data['goods_num'], data['goods_id']])
        return JsonResponse.success(msg='修改成功') if not isOk else JsonResponse.fail(msg='商品编号不可修改')

    @app.route("/delete_goods", methods=["DELETE"])  # 删除（单个）
    @log_route
    def delete_goods():
        # request.args获取请求链接中 ? 后面的所有参数；以字典的方式存储
        if 'goods_id' not in request.args:
            return JsonResponse.fail(msg='需要传入goods_id')
        isOk = db.execute(sql='delete from goods where goods_id=%s', args=[request.args['goods_id']])
        return JsonResponse.success(msg='删除成功') if not isOk else JsonResponse.fail(msg='删除失败')
