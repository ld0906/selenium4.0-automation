from selenium import webdriver

'''
函数 return_driver是为了返回driver对象
'''
def return_driver(browser_type):
    browser_des = None
    if browser_type == "firefox":
        browser_des = webdriver.DesiredCapabilities.FIREFOX.copy()
    elif browser_type == "chrome":
        browser_des = webdriver.DesiredCapabilities.CHROME.copy()

    browser_des["platform"] = "LINUX"
    return webdriver.Remote('http://localhost:4444/wd/hub',desired_capabilities=browser_des)
