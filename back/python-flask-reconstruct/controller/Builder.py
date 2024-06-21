from flask import Flask
from flask_cors import CORS
from json_flask import *
from .client_controller import client_route
from .good_controller import good_route
from .purchase_controller import purchase_route
from .sale_controller import sale_route
from .staff_controller import staff_route
from .login_controller import login_route

# 同一个表的路由放在同一个文件
class Builder():
    def build_Flask(self, name):
        pass
    def build_CORS(self):
        pass
    def build_login_route(self):
        pass
    def build_client_route(self):
        pass
    def build_staff_route(self):
        pass
    def build_good_route(self):
        pass
    def build_purchase_route(self):
        pass
    def build_sale_route(self):
        pass



class CCBuilder(Builder):
    def __init__(self):
        super().__init__()
        self.app = JsonFlask('')

    # 创建 Flask 对象并初始化
    def build_Flask(self, name):
        self.app.import_name = name
    
    # 为应用程序初始化跨源资源共享
    def build_CORS(self):
        CORS(self.app, supports_credentials=True)

    def build_login_route(self):
        print('registe login route')
        login_route(self.app)

    def build_client_route(self):
        client_route(self.app)

    def build_staff_route(self):
        staff_route(self.app)

    def build_good_route(self):
        good_route(self.app)

    def build_purchase_route(self):
        purchase_route(self.app)

    def build_sale_route(self):
        sale_route(self.app)

    # 返回构建的 Flask 对象
    def get_result(self):
        return self.app
    
# 主管类
class Director:
    def construct_main_controller(self, builder):
        builder.build_Flask('__main__')
        builder.build_CORS()
        builder.build_login_route()
        builder.build_client_route()
        builder.build_staff_route()
        builder.build_good_route()
        builder.build_purchase_route()
        builder.build_sale_route()

# 中枢控制器
class CentralController:
    # 为主模块 main 创建Flask对象，并注册视图函数
    def __init__(self):
        ccdirector = Director()
        ccbuilder = CCBuilder()
        ccdirector.construct_main_controller(ccbuilder)
        self.app = ccbuilder.get_result()
        print("Successfully create an app!")

    # 指定self.app在特定端口运行
    def run(self, host, port, debug):
        self.app.run(host=host, port=port, debug=debug)

    def __del__(self):
        print("Successfully destroy the app!")