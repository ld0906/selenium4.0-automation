from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time,os

#这是在mac上执行的基于chrome浏览器上的测试，如下driver地址请根据实际情况进行修改。
#chrome_driver_server = Service("/Users/jason118/Downloads/chromedriver")

driver  = webdriver.Chrome(service=chrome_driver_server)
driver.get("http://testdao.site/index")

time.sleep(15)

#点击左侧导航栏->系统管理
driver.find_element(By.XPATH,'//*[@id="side-menu"]/li[3]/a/span[1]').click()

time.sleep(5)

#点击左侧导航栏，系统管理次级菜单->岗位管理
driver.find_element(By.XPATH,'//*[@id="side-menu"]/li[3]/ul/li[5]/a').click()
time.sleep(2)

#点击新增超链接
#切换driver到iframe，因为新增超链接是在iframe内。
driver.switch_to.frame("iframe6")
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="toolbar"]/a[1]').click()
time.sleep(2)

#首先返回到主页，释放iframe
driver.switch_to.default_content()
#再次进入另外的新的iframe
driver.switch_to.frame("layui-layer-iframe1")
#在添加岗位页面，输入岗位名称
driver.find_element(By.NAME,'postName').send_keys('Post1')
# #在添加岗位页面，输入岗位编码
driver.find_element(By.NAME,'postCode').send_keys('PostCode1')
# #在添加岗位页面，输入显示顺序
driver.find_element(By.NAME,'postSort').send_keys('1')

# #在添加岗位页面，输入备注

driver.find_element(By.NAME,'remark').send_keys("remark text 1")

#首先返回到主页，释放iframe
time.sleep(3)
driver.switch_to.default_content()

# #在添加岗位页面，点击确定按钮
driver.find_element(By.XPATH,'//*[@id="layui-layer1"]/div[3]/a[1]').click()
time.sleep(5)
