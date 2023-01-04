from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.baidu.com")


# echo 'export PATH=$PATH:真实的driver路径' >> ~/.bash_profile
# source ~/.bash_profile
