"""
The State Pattern is inspired by code from 
https://github.com/Supremacy-ysyyrps/SoftwareEngineering/blob/aea6e52aba3b231a2546015ad0827321f26ff46b/code/rear-end/dal/database.py#L73
"""

class State:
    def __init__(self, database):
        self.db = database
    def exe(self, cmd):
        pass
    def roll(self):
        pass
    def fetch(self):
        pass
    def commit(self):
        pass

class ExeState(State):
    def __init__(self, database):
        super().__init__(database)
    def exe(self, cmd, args):
        self.db.cursor.execute(cmd, args)
        print('executing sql')

class RollState(State):
    def __init__(self, database):
        super().__init__(database)
    def roll(self):
        self.db.conn.rollback()
        print('rollback successfully')


class FetchState(State):
    def __init__(self, database):
        super().__init__(database)
    def fetch(self):
        try:
            # 如果有查询结果，返回查询结果
            return self.db.cursor.fetchall()
        # 如果没有返回结果（如增删改），则捕捉抛出的异常，返回None
        except Exception as e:
            return '提取信息失败'


class CommitState(State):
    def __init__(self, database):
        super().__init__(database)
    def commit(self):
        # 使用con.commit()提交事务，使数据持久化
        print('commit successfully')
        self.db.conn.commit()