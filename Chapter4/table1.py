from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

#这是在mac上执行的基于chrome浏览器上的测试，如下driver地址请根据实际情况进行修改。
chrome_driver_server = Service("/Users/jason118/Downloads/chromedriver")
driver  = webdriver.Chrome(service=chrome_driver_server)

#如下是打开本地文件，请根据实际地址进行改写
driver.get("file:///Users/jason118/PycharmProjects/selenium4.0-automation/Chapter4/table1.html")

#通过id定位方式获取整个表格对象
html_table = driver.find_element(By.ID,"table1")

#通过元素名（标签）获取表格中所有的行对象
tr_list = html_table.find_elements(By.TAG_NAME,"tr")
th_cols = tr_list[0].find_elements(By.TAG_NAME,"th")
for col in th_cols:
    print(col.text+"\t",end='')
print()

for i in range(1,len(tr_list)):
    td_cols = tr_list[i].find_elements(By.TAG_NAME,"td")
    for c in td_cols:
        print(c.text+"\t",end='')
    print()

driver.quit()
