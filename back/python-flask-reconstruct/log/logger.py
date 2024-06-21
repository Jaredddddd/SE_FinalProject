import functools
import logging
from flask import Flask, request, jsonify

# 配置日志记录器
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# 创建一个控制台处理器
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# 创建一个文件处理器
file_handler = logging.FileHandler('./app.log', mode='a')
file_handler.setLevel(logging.INFO)

# 创建格式器
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 为处理器设置格式
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# 将处理器添加到记录器
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# 路由日志
def log_route(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f'Route accessed: {request.path}')
        logger.info(f'Method: {request.method}')
        logger.info(f'Args: {request.args}')
        logger.info(f'Form: {request.form}')
        logger.info(f'JSON: {request.json}')
        response = func(*args, **kwargs)
        # print(response)
        logger.info(f'Response: {response.to_dict()}')
        return response
    return wrapper


