#coding=utf-8
import unittest
import  threading
from thred_unit.basic_case import ParaCase
from thred_unit.basic_case import DetailCase
from selenium import webdriver

#本例实现本地多个浏览器对同一脚本并发操作
#继承父类threading.Thread
class myThread (threading.Thread):   
    def __init__(self, device):
        threading.Thread.__init__(self)
        self.device=device

    def run(self):
        print ("Starting " + self.name)
        print ("Exiting " + self.name)
        run_suite(self.device)
#定义多线程实际要执行的操作
def run_suite(device):
    suite = unittest.TestSuite()
    suite.addTest(ParaCase.parametrize(DetailCase, param=device))
unittest.TextTestRunner(verbosity=1).run(suite)

if __name__ == '__main__':
    #以下代是在本地通过同时访问多浏览器
    dr = [webdriver.Firefox(executable_path='需要输入正确的firefox webdriver路径'), webdriver.Chrome('需要输入正确的Chrome webdriver路径’)]
    for i in range(len(dr)):
        print(dr[i])
        th = myThread(dr[i])
        th.start()
        th.join()
