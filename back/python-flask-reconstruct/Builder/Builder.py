from flask import Flask
from flask_cors import CORS
from json_flask import *
from .client_builder import client_route
from .good_builder import good_route
from .purchase_builder import purchase_route
from .sale_builder import sale_route
from .staff_builder import staff_route
from .login_builder import login_route
from .register_builder import register_route

# 同一个表的路由放在同一个文件
class Builder():
    def build_Flask(self, name):
        pass
    def build_CORS(self):
        pass
    def buildLoginRoute(self):
        pass
    def buildClientRoute(self):
        pass
    def buildStaffRoute(self):
        pass
    def buildGoodRoute(self):
        pass
    def buildPurchaseRoute(self):
        pass
    def buildSaleRoute(self):
        pass
    def buildRegisterRoute(self):
        pass



class RouteBuilder(Builder):
    def __init__(self):
        super().__init__()
        self.app = JsonFlask('')

    # 创建 Flask 对象并初始化
    def build_Flask(self, name):
        self.app.import_name = name
    
    # 为应用程序初始化跨源资源共享
    def build_CORS(self):
        CORS(self.app, supports_credentials=True)

    def buildLoginRoute(self):
        login_route(self.app)

    def buildClientRoute(self):
        client_route(self.app)

    def buildStaffRoute(self):
        staff_route(self.app)

    def buildGoodRoute(self):
        good_route(self.app)

    def buildPurchaseRoute(self):
        purchase_route(self.app)

    def buildSaleRoute(self):
        sale_route(self.app)

    def buildRegisterRoute(self):
        register_route(self.app)

    # 返回构建的 Flask 对象
    def get_result(self):
        return self.app

class App:
    # 为主模块 main 创建Flask对象，并注册视图函数
    def __init__(self):
        routebuilder = RouteBuilder()
        routebuilder.build_Flask('__main__')
        routebuilder.build_CORS()
        routebuilder.buildLoginRoute()
        routebuilder.buildClientRoute()
        routebuilder.buildStaffRoute()
        routebuilder.buildGoodRoute()
        routebuilder.buildPurchaseRoute()
        routebuilder.buildSaleRoute()
        routebuilder.buildRegisterRoute()
        self.app = routebuilder.get_result()

    # 指定self.app在特定端口运行
    def run(self, host, port, debug):
        self.app.run(host=host, port=port, debug=debug)

    def __del__(self):
        """
        类实例销毁时的钩子函数。
        
        当类的实例被垃圾回收器回收时，这个方法会被调用。它主要用于执行一些清理工作或输出一些信息。
        本例中，它用于提示应用程序已被成功销毁。
        """
        print("Successfully destroy the app!")