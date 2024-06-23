import unittest
from unittest.mock import patch
from datetime import datetime
from controller.Builder import CentralController
ip = '0.0.0.0'
port = 666
app = CentralController()
print('-----------------start testing-----------------')

class TestGoodRoute(unittest.TestCase):

    def setUp(self):
        self.app = app.app
        self.client = self.app.test_client()

    @patch('database.database.db.execute')
    def test_all_goods(self, mock_execute):
        # 模拟db.execute的返回值
        mock_execute.return_value = [{'goods_id': 1, 'goods_name': 'item1', 'goods_num': 100}]

        response = self.client.get('/all_goods')
        # 获取JsonResponse对象并转换为字典
        json_response = response.get_json()  # 从响应中正确获取JSON数据
        print(json_response)

        self.assertTrue(isinstance(json_response, dict))
        self.assertEqual(json_response['msg'], '查询成功')
        self.assertIn('data', json_response)

    @patch('database.database.db.execute')
    def test_add_goods(self, mock_execute):
        # 模拟db.execute的返回值
        mock_execute.return_value = 0  # 表示插入成功

        data = {
            'goods_id': 2,
            'goods_name': 'item2',
            'goods_num': 50
        }

        response = self.client.post('/add_goods', json=data)
        json_response = response.get_json()
        print(json_response)

        self.assertTrue(isinstance(json_response, dict))
        self.assertEqual(json_response['msg'], '添加成功')
        self.assertIn('data', json_response)

    @patch('database.database.db.execute')
    def test_update_goods(self, mock_execute):
        # 模拟db.execute的返回值
        mock_execute.return_value = 0  # 表示更新成功

        data = {
            'goods_id': 2,
            'goods_name': 'updated_item2',
            'goods_num': 60
        }

        response = self.client.put('/update_goods', json=data)
        json_response = response.get_json()
        print(json_response)

        self.assertTrue(isinstance(json_response, dict))
        self.assertEqual(json_response['msg'], '修改成功')
        self.assertIn('data', json_response)

    @patch('database.database.db.execute')
    def test_delete_goods(self, mock_execute):
        # 模拟db.execute的返回值
        mock_execute.return_value = 0  # 表示删除成功

        response = self.client.delete('/delete_goods', query_string={'goods_id': 2})
        json_response = response.get_json()
        print(json_response)

        self.assertTrue(isinstance(json_response, dict))
        self.assertEqual(json_response['msg'], '删除成功')
        self.assertIn('data', json_response)
class TestClientRoute(unittest.TestCase):

    def setUp(self):
        app = CentralController()
        self.app = app.app
        self.client = self.app.test_client()

    @patch('database.database.db.execute')
    def test_all_client(self, mock_execute):
        # 模拟db.execute的返回值
        mock_execute.return_value = [{'client_id': '1', 'client_name': 'John Doe', 'phone_number': '12345678901', 'address': '123 Main St'}]

        response = self.client.get('/all_client')
        json_response = response.get_json()  # 从响应中正确获取JSON数据
        print(json_response)

        self.assertTrue(isinstance(json_response, dict))
        self.assertEqual(json_response['msg'], '查询成功')
        self.assertIn('data', json_response)

    @patch('database.database.db.execute')
    def test_add_client(self, mock_execute):
        # 模拟db.execute的返回值
        mock_execute.return_value = 0  # 表示插入成功

        data = {
            'client_id': '2',
            'client_name': 'Jane Doe',
            'phone_number': '09876543210',
            'address': '456 Main St'
        }

        response = self.client.post('/add_client', json=data)
        json_response = response.get_json()
        print(json_response)

        self.assertTrue(isinstance(json_response, dict))
        self.assertEqual(json_response['msg'], '添加成功')
        self.assertIn('data', json_response)

    @patch('database.database.db.execute')
    def test_update_client(self, mock_execute):
        # 模拟db.execute的返回值
        mock_execute.return_value = 0  # 表示更新成功

        data = {
            'client_id': '2',
            'client_name': 'Jane Doe Updated',
            'phone_number': '09876543211',
            'address': '456 Main St Updated'
        }

        response = self.client.put('/update_client', json=data)
        json_response = response.get_json()
        print(json_response)

        self.assertTrue(isinstance(json_response, dict))
        self.assertEqual(json_response['msg'], '修改成功')
        self.assertIn('data', json_response)

    @patch('database.database.db.execute')
    def test_delete_client(self, mock_execute):
        # 模拟db.execute的返回值
        mock_execute.return_value = 0  # 表示删除成功

        response = self.client.delete('/delete_client', query_string={'client_id': '2'})
        json_response = response.get_json()
        print(json_response)

        self.assertTrue(isinstance(json_response, dict))
        self.assertEqual(json_response['msg'], '删除成功')
        self.assertIn('data', json_response)
class TestLoginRoute(unittest.TestCase):

    def setUp(self):
        app = CentralController()
        self.app = app.app
        self.client = self.app.test_client()

    @patch('database.database.db.execute')
    def test_login_success(self, mock_execute):
        # 模拟db.execute的返回值
        mock_execute.return_value = [{'password': 'correct_password', 'identity': 'manager'}]

        data = {
            'username': 'test_user',
            'password': 'correct_password'
        }

        response = self.client.post('/login', json=data)
        json_response = response.get_json()
        print(json_response)

        self.assertTrue(isinstance(json_response, dict))
        self.assertEqual(json_response['msg'], '登录成功')
        self.assertIn('data', json_response)
        self.assertEqual(json_response['data']['username'], 'test_user')
        self.assertEqual(json_response['data']['identity'], 'manager')

    @patch('database.database.db.execute')
    def test_login_fail_incorrect_password(self, mock_execute):
        # 模拟db.execute的返回值
        mock_execute.return_value = [{'password': 'correct_password', 'identity': 'manager'}]

        data = {
            'username': 'test_user',
            'password': 'wrong_password'
        }

        response = self.client.post('/login', json=data)
        json_response = response.get_json()
        print(json_response)

        self.assertTrue(isinstance(json_response, dict))
        self.assertEqual(json_response['msg'], '登录失败,请重新输入账号和密码')
        self.assertIsNone(json_response['data'])  # 修改断言，验证 data 是 None

    @patch('database.database.db.execute')
    def test_login_fail_user_not_found(self, mock_execute):
        # 模拟db.execute的返回值为空表示用户不存在
        mock_execute.return_value = []

        data = {
            'username': 'non_existent_user',
            'password': 'any_password'
        }

        response = self.client.post('/login', json=data)
        json_response = response.get_json()
        print(json_response)

        self.assertTrue(isinstance(json_response, dict))
        self.assertEqual(json_response['msg'], '登录失败,请重新输入账号和密码')
        self.assertIsNone(json_response['data'])  # 修改断言，验证 data 是 None
class TestPurchaseRoute(unittest.TestCase):

    def setUp(self):
        app = CentralController()
        self.app = app.app
        self.client = self.app.test_client()

    @patch('database.database.db.execute')
    def test_all_purchase(self, mock_execute):
        # 模拟db.execute的返回值
        mock_execute.return_value = [
            {'purchase_id': 'P001', 'goods_id': 'G001', 'staff_id': 'S001',
             'purchase_price': 100.0, 'purchase_num': 5, 'purchase_amount': 500.0,
             'purchase_date': datetime(2024, 6, 23).date()}
        ]

        response = self.client.get('/all_purchase')
        json_response = response.get_json()
        print(json_response)

        self.assertTrue(isinstance(json_response, dict))
        self.assertEqual(json_response['msg'], '查询成功')
        self.assertIn('data', json_response)
        self.assertEqual(len(json_response['data']), 1)

    @patch('database.database.db.execute')
    def test_add_purchase(self, mock_execute):
        # 模拟db.execute的返回值，假设添加成功返回空列表
        mock_execute.return_value = []

        data = {
            'purchase_id': 'P001',
            'goods_id': 'G001',
            'staff_id': 'S001',
            'purchase_price': 100.0,
            'purchase_num': 5,
            'purchase_amount': 500.0,
            'purchase_date': '2024-06-23'
        }

        response = self.client.post('/add_purchase', json=data)
        json_response = response.get_json()
        print(json_response)

        self.assertTrue(isinstance(json_response, dict))
        self.assertEqual(json_response['msg'], '添加成功')
        self.assertIsNone(json_response['data'])

    @patch('database.database.db.execute')
    def test_update_purchase(self, mock_execute):
        # 模拟db.execute的返回值，假设更新成功返回空列表
        mock_execute.return_value = []

        data = {
            'purchase_id': 'P001',
            'goods_id': 'G002',  # 修改 goods_id
            'staff_id': 'S002',  # 修改 staff_id
            'purchase_price': 120.0,  # 修改 purchase_price
            'purchase_num': 7,  # 修改 purchase_num
            'purchase_amount': 840.0,  # 修改 purchase_amount
            'purchase_date': '2024-06-23'
        }

        response = self.client.put('/update_purchase', json=data)
        json_response = response.get_json()
        print(json_response)



    @patch('database.database.db.execute')
    def test_delete_purchase(self, mock_execute):
        # 模拟db.execute的返回值，假设删除成功返回空列表
        mock_execute.return_value = []

        params = {'purchase_id': 'P001'}

        response = self.client.delete('/delete_purchase', query_string=params)
        json_response = response.get_json()
        print(json_response)

        self.assertTrue(isinstance(json_response, dict))
        self.assertEqual(json_response['msg'], '删除成功')
        self.assertIsNone(json_response['data'])
class TestSaleRoute(unittest.TestCase):

    def setUp(self):
        app = CentralController()
        self.app = app.app
        self.client = self.app.test_client()

    @patch('database.database.db.execute')
    def test_all_sale(self, mock_execute):
        # 模拟db.execute的返回值
        mock_execute.return_value = [
            {'sale_id': 'S001', 'client_id': 'C001', 'goods_id': 'G001',
             'sale_price': 120.0, 'sale_num': 5, 'sale_amount': 600.0,
             'sale_date': datetime(2024, 6, 23).date()}
        ]

        response = self.client.get('/all_sale')
        json_response = response.get_json()
        print(json_response)

        self.assertTrue(isinstance(json_response, dict))
        self.assertEqual(json_response['msg'], '查询成功')
        self.assertIn('data', json_response)
        self.assertEqual(len(json_response['data']), 1)

    @patch('database.database.db.execute')
    def test_add_sale(self, mock_execute):
        # 模拟db.execute的返回值，假设添加成功返回空列表
        mock_execute.return_value = []

        data = {
            'sale_id': 'S001',
            'client_id': 'C001',
            'goods_id': 'G001',
            'sale_price': 120.0,
            'sale_num': 5,
            'sale_amount': 600.0,
            'sale_date': '2024-06-23'
        }

        response = self.client.post('/add_sale', json=data)
        json_response = response.get_json()
        print(json_response)

        self.assertTrue(isinstance(json_response, dict))
        self.assertEqual(json_response['msg'], '销售表添加成功')
        self.assertIsNone(json_response['data'])

    @patch('database.database.db.execute')
    def test_update_sale(self, mock_execute):
        # 模拟db.execute的返回值，假设更新成功返回空列表
        mock_execute.return_value = []

        data = {
            'sale_id': 'S001',
            'client_id': 'C002',  # 修改 client_id
            'goods_id': 'G002',  # 修改 goods_id
            'sale_price': 130.0,  # 修改 sale_price
            'sale_num': 6,  # 修改 sale_num
            'sale_amount': 780.0,  # 修改 sale_amount
            'sale_date': '2024-06-23'
        }

        response = self.client.put('/update_sale', json=data)
        json_response = response.get_json()
        print(json_response)



    @patch('database.database.db.execute')
    def test_delete_sale(self, mock_execute):
        # 模拟db.execute的返回值，假设删除成功返回空列表
        mock_execute.return_value = []

        params = {'sale_id': 'S001'}

        response = self.client.delete('/delete_sale', query_string=params)
        json_response = response.get_json()
        print(json_response)

        self.assertTrue(isinstance(json_response, dict))
        self.assertEqual(json_response['msg'], '销售表删除成功')
        self.assertIsNone(json_response['data'])
class TestStaffRoute(unittest.TestCase):

    def setUp(self):
        app = CentralController()
        self.app = app.app
        self.client = self.app.test_client()

    @patch('database.database.db.execute')
    def test_all_staff(self, mock_execute):
        # 模拟db.execute的返回值
        mock_execute.return_value = [
            {'staff_id': 'S001', 'staff_name': 'John Doe', 'department': 'HR',
             'salary': 5000.0, 'phone_number': '1234567890'}
        ]

        response = self.client.get('/all_staff')
        json_response = response.get_json()
        print(json_response)

        self.assertTrue(isinstance(json_response, dict))
        self.assertEqual(json_response['msg'], '查询成功')
        self.assertIn('data', json_response)
        self.assertEqual(len(json_response['data']), 1)

    @patch('database.database.db.execute')
    def test_add_staff(self, mock_execute):
        # 模拟db.execute的返回值，假设添加成功返回空列表
        mock_execute.return_value = []

        data = {
            'staff_id': 'S002',
            'staff_name': 'Jane Doe',
            'department': 'IT',
            'salary': 6000.0,
            'phone_number': '9876543210'
        }

        response = self.client.post('/add_staff', json=data)
        json_response = response.get_json()
        print(json_response)

        self.assertTrue(isinstance(json_response, dict))
        self.assertEqual(json_response['msg'], '添加成功')
        self.assertIsNone(json_response['data'])

    @patch('database.database.db.execute')
    def test_update_staff(self, mock_execute):
        # 模拟db.execute的返回值，假设更新成功返回空列表
        mock_execute.return_value = []

        data = {
            'staff_id': 'S001',
            'staff_name': 'John Smith',  # 修改 staff_name
            'department': 'Finance',  # 修改 department
            'salary': 5500.0,  # 修改 salary
            'phone_number': '9876543210'  # 修改 phone_number
        }

        response = self.client.put('/update_staff', json=data)
        json_response = response.get_json()
        print(json_response)

        self.assertTrue(isinstance(json_response, dict))
        self.assertEqual(json_response['msg'], '修改成功')
        self.assertIsNone(json_response['data'])

    @patch('database.database.db.execute')
    def test_delete_staff(self, mock_execute):
        # 模拟db.execute的返回值，假设删除成功返回空列表
        mock_execute.return_value = []

        params = {'staff_id': 'S001'}

        response = self.client.delete('/delete_staff', query_string=params)
        json_response = response.get_json()
        print(json_response)

        self.assertTrue(isinstance(json_response, dict))
        self.assertEqual(json_response['msg'], '删除成功')
        self.assertIsNone(json_response['data'])
class TestRegisterRoute(unittest.TestCase):

    def setUp(self):
        app = CentralController()
        self.app = app.app
        self.client = self.app.test_client()

    @patch('database.database.db.execute')
    def test_register_success(self, mock_execute):
        # 模拟db.execute的返回值，假设注册成功返回空列表
        mock_execute.return_value = []

        data = {
            'username': 'test_user',
            'password': 'test_password',
            'identity': 'manager'
        }

        response = self.client.post('/register', json=data)
        json_response = response.get_json()
        print(json_response)

        self.assertTrue(isinstance(json_response, dict))
        self.assertEqual(json_response['msg'], '注册成功')
        self.assertIsNone(json_response['data'])

    @patch('database.database.db.execute')
    def test_register_username_exists(self, mock_execute):
        # 模拟db.execute的返回值，假设用户名已存在返回非空列表
        mock_execute.return_value = [{'username': 'existing_user'}]

        data = {
            'username': 'existing_user',
            'password': 'test_password',
            'identity': 'saler'
        }

        response = self.client.post('/register', json=data)
        json_response = response.get_json()
        print(json_response)

        self.assertTrue(isinstance(json_response, dict))
        self.assertEqual(json_response['msg'], '用户名已存在，请选择其他用户名')
        self.assertIsNone(json_response['data'])

    def test_register_username_empty(self):
        data = {
            'username': '',
            'password': 'test_password',
            'identity': 'buyer'
        }

        response = self.client.post('/register', json=data)
        json_response = response.get_json()
        print(json_response)

        self.assertTrue(isinstance(json_response, dict))
        self.assertEqual(json_response['msg'], '用户名不能为空')
        self.assertIsNone(json_response['data'])

    def test_register_password_empty(self):
        data = {
            'username': 'test_user',
            'password': '',
            'identity': 'manager'
        }

        response = self.client.post('/register', json=data)
        json_response = response.get_json()
        print(json_response)

        self.assertTrue(isinstance(json_response, dict))
        self.assertEqual(json_response['msg'], '密码不能为空')
        self.assertIsNone(json_response['data'])

    def test_register_identity_empty(self):
        data = {
            'username': 'test_user',
            'password': 'test_password',
            'identity': ''
        }

        response = self.client.post('/register', json=data)
        json_response = response.get_json()
        print(json_response)

        self.assertTrue(isinstance(json_response, dict))
        self.assertEqual(json_response['msg'], '身份不能为空')
        self.assertIsNone(json_response['data'])

if __name__ == '__main__':

    unittest.main()
