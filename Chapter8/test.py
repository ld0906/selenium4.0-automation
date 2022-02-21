from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from PIL import Image
import time
import pytesseract

#这是在mac上执行的基于chrome浏览器上的测试，如下driver地址请根据实际情况进行修改。
chrome_driver_server = Service("/Users/jason118/Downloads/chromedriver")
driver  = webdriver.Chrome(service=chrome_driver_server)

driver.get("http://testdao.site/login")

driver.get_screenshot_as_file("capture.png")

loc = driver.find_element(By.XPATH,'//*[@id="signupForm"]/div[1]/div[2]/a/img').location

size = driver.find_element(By.XPATH,'//*[@id="signupForm"]/div[1]/div[2]/a/img').size

left = loc['x']
top = loc['y']
right = loc['x'] + size['width']
bottom = loc['y'] + size['height']

img = Image.open("capture.png").crop((left,top,right,bottom))

code = pytesseract.image_to_string(img)
print(code.strip())

# img = driver.find_element(By.XPATH,'//*[@id="signupForm"]/div[1]/div[2]/a/img')
# img.screenshot('capture.png')
#
#
# img1 = Image.open(img)
# code = pytesseract.image_to_string(img1)
# print(code.strip())



#https://blog.csdn.net/zhu940923/article/details/81264542

