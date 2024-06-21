import pymysql
from .config import DB_CONFIG
from .database_state import *

class SQLManager(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        """
        实现单例模式的 __new__ 方法。
        
        这个方法确保无论多少次调用，都只返回同一个实例对象。当第一次调用时，创建一个新的实例，
        并将其存储在类的 _instance 属性中。后续调用将直接返回已存在的实例。
        
        参数:
        cls -- 类对象，这个方法是属于这个类的。
        *args -- 位置参数，传递给类的构造函数。
        **kwargs -- 关键字参数，传递给类的构造函数。
        
        返回:
        类的实例，如果是第一次调用，则是一个新实例；否则，返回已存在的实例。
        """
        # 检查类的 _instance 属性是否已经初始化
        if not cls._instance:
            # 如果 _instance 未初始化，调用超类的 __new__ 方法来创建一个新的实例
            cls._instance = super(SQLManager, cls).__new__(cls, *args, **kwargs)
        # 返回类的 _instance 属性，无论是否是新创建的
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_initialized'):
            self.conn = None
            self.cursor = None
            self.state = ExeState(self)
            self.connect()
            self._initialized = True

    # 连接数据库
    def connect(self):
        # 建立连接
        self.conn = pymysql.connect(
            host=DB_CONFIG["host"],
            port=DB_CONFIG["port"],
            user=DB_CONFIG["user"],
            passwd=DB_CONFIG["passwd"],
            db=DB_CONFIG["db"],
            charset=DB_CONFIG["charset"]
        )
        # 获取游标对象；pymysql.cursors.DictCursor指定返回的结果类型为字典，默认是元组类型
        # 在连接没有关闭之前，游标对象可以反复使用
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
    # 状态模式
    def change_state(self, state):
        self.state = state
    
    # 执行函数，用来处理各种状态
    def execute(self, sql, args=None):
        # 尝试执行SQL命令
        try:
            self.change_state(ExeState(self))
            self.state.exe(sql, args)
        # 如果出现执行异常（如违反约束等），回滚事务后返回异常
        except Exception as e:
            print(f'exception: {e}')
            self.change_state(RollState(self))
            self.state.roll()
            return e
        # 若没有执行异常，取回查询结果或None
        else:
            self.change_state(FetchState(self))
            return self.state.fetch()
        # 最终提交事务
        finally:
            self.change_state(CommitState(self))
            self.state.commit()
    # 关闭数据库cursor和连接(这里可以加log)
    def close(self):
        self.cursor.close()
        self.conn.close()



db = SQLManager()