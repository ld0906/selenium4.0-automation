#coding=utf-8
from com.page.base import  Base
from selenium.webdriver.common.by import  By
import time
#loginPage继承了Base类
class loginPage(Base):
	#以下为类的初始化函数，其又调用了父类的初始化函数，这样做的目的是为了
	#将context.driver串起来，在调用PO类时，可以使用超级全局变量context下的driver对象
    def __init__(self,context):
        super(loginPage,self).__init__(context.driver)
    def login(self,username,password):
        self.findele(By.NAME,"username").clear()
        self.findele(By.NAME,"username").send_keys(username)
        self.findele(By.NAME,"password").clear()
        self.findele(By.NAME,"password").send_keys(password)


