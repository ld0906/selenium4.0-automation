from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import xlrd
import logging

chrome_driver_server = Service("./chromedriver")
driver  = webdriver.Chrome(service=chrome_driver_server)

'''
函数 return_driver是为了返回driver对象
'''
def return_driver():
    return driver

'''
函数 name是为了用NAME方式来定位元素
'''
def name(locator):
    return driver.find_element(By.NAME,locator)

'''
函数 id是为了用ID方式来定位元素
'''
def id(locator):
    return driver.find_element(By.ID,locator)

'''
函数 xpath是为了用XPATH方式来定位元素
'''
def xpath(locator):
    return driver.find_element(By.XPATH,locator)


#这是新添加的函数，用于处理和获取Excel文件中的测试数据。
def read_excel(filename,index):
    xls = xlrd.open_workbook(filename)
    sheet = xls.sheet_by_index(index)
    #print(sheet.nrows)
    #print(sheet.ncols)
    dic={}
    for j in range(sheet.ncols):

        data=[]
        for i in range(sheet.nrows):
          data.append(sheet.row_values(i)[j])
        dic[j]=data
    return dic

def log(str):
    logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='log-selenium.log',
                    filemode='a')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)
    logging.info(str)
