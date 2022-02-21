from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

#这是在mac上执行的基于chrome浏览器上的测试，如下driver地址请根据实际情况进行修改。
chrome_driver_server = Service("/Users/jason118/Downloads/chromedriver")
driver = webdriver.Chrome(service=chrome_driver_server)
driver.maximize_window()
driver.get('https://www.cnblogs.com') #打开博客园主页面，首先在验证这个例子之前需要先注册好博客园账户。
#根据之前打印出来的登录博客园之后的cookie情况在此次手动添加cookie，这种方式可以跳过验证码。
#下面的cookie的value值，只需要设置为之前登录后抓到的相应的值即可，可以重复利用，测试过，自动登录功能可行。
driver.add_cookie({'domain': '.cnblogs.com','name': '.CNBlogsCookie','value': ''})
driver.add_cookie({'domain': '.cnblogs.com','name': '.Cnblogs.AspNetCore.Cookies','value': ''})
time.sleep(3)
driver.refresh() #页面刷新。
time.sleep(3)
driver.quit()
