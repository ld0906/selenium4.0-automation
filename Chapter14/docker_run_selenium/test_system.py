import threading
from login import login

#测试权限系统登录场景
def test_login(browser_type):
    login(browser_type)

if __name__ == '__main__':
    browser_set = ("chrome","firefox")
    for bt in browser_set:
        #实现多线程并发测试多浏览器测试需求
        threading.Thread(target=test_login,args=(bt,)).start()
