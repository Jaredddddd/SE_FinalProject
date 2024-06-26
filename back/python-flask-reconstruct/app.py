from flask import request
from flask_cors import *

from json_flask import JsonFlask
from json_response import JsonResponse
from database.database import SQLManager
from datetime import datetime
import json
from Builder.Builder import App

"""
建造者模式： App
修饰器模式： logger
单例模式： SQLManager 
状态模式： State(4个状态)
适配器: JsonResponse
"""

# # 创建视图应用，使用改造后的JsonFlask对象
# app = JsonFlask(__name__)

# # 解决跨域
# CORS(app, supports_credentials=True)

# # 数据库连接对象
# db = SQLManager()

# builder 
ip = '0.0.0.0'
port = 666
app = App()
app.run(host=ip, port=port, debug=True)

