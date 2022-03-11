#coding=utf-8
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
#以下函数为了实现打开网站的操作
@when('I open the login website')
def step_impl(context):
    #请在下列代码中添加真实的chromedriver的路径  
    chrome_driver_server = Service("/Users/jason118/PycharmProjects/selenium4.0-automation/Chapter12/Chapter12.3/steps/chromedriver")
    context.driver  = webdriver.Chrome(service=chrome_driver_server)
    #context.driver = webdriver.Chrome("xxx")
    context.driver.get('http://testdao.site/login')
#以下的函数是为了实现输入用户名
@Then('I input username')
def step_i2(context):  
    context.driver.find_element(By.NAME,"username").clear()
    context.driver.find_element(By.NAME,"username").send_keys("admin")

#以下的函数是为了实现输入密码
@Then('I input password')
def step_i3(context): 
    context.driver.find_element(By.NAME,"password").clear()
    context.driver.find_element(By.NAME,"password").send_keys("admin123")

