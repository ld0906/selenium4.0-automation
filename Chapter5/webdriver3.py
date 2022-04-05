from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_service = Service(executable_path='./chromedriver')
driver = webdriver.Chrome(service=chrome_service)
driver.get("https://www.baidu.com")