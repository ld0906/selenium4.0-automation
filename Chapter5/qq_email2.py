from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#这是在mac上执行的基于chrome浏览器上的测试，如下driver地址请根据实际情况进行修改。
chrome_driver_server = Service("/Users/jason118/Downloads/chromedriver")
driver=webdriver.Chrome(service=chrome_driver_server)
driver.maximize_window()
driver.get('https://en.mail.qq.com/cgi-bin/loginpage') #打开主页面'QQ邮箱登录页面'
driver.switch_to.frame("login_frame") #将驱动转向iframe,使得selneium目前可以定位iframe内部的元素，此次定位的方式是通过iframe id属性定位得到。
driver.find_element(By.ID,'u').send_keys('test')#在iframe内，定位QQ邮箱地址输入框，并赋值'test'
driver.switch_to.default_content() #此步的目的使driver的焦点切回主界面，不在将焦点放在iframe中。
#driver.quit() #退出浏览器操作
print('test complete!') #打印"测试完成"标记。