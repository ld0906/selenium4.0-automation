from  ddt import  ddt ,data,file_data,unpack
from dataexcel import get_data
import unittest

#data_excel ={'0': ['上海', '杭州', '20190105', ''], '1': ['南京', '杭州', '20190105', '小王']}
#ex=[{"username": "tim","pwd": "123456"},{"username": "tim1","pwd": "123456"}]
#调用封装的读取excel方法,文件路径因在代码中写死，故传空值
#本功能可用于多轮数据重复性测试
ex=get_data('', 1)
@ddt
class test_se(unittest.TestCase):
    @data(*ex)
    def test_01(self,dic):
        print(dic)
        print(dic.values())
        print(dic.get('username'))
        self.assertEqual("selenium",dic.get('username'))

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()