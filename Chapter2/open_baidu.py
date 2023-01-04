#引入python自带的os代码模块
import os
#导入WebDriver模块和Service类，
#其中Service类是4.0版本引入的新用法
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#设置IE浏览器的WebDriver驱动程序路径
ie_driver_server = Service("C:\\Program Files (x86)\\Internet Explorer\\IEDriverServer.exe")

#启动IE浏览器
driver =  webdriver.Ie(service=ie_driver_server)

#打开百度首页
driver.get('https://www.baidu.com')
driver.quit() #退出浏览器