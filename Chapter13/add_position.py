import time,os
from functions import return_driver,name,id,xpath


def add_position(postName,postCode):
    driver = return_driver()
    driver.get("http://124.223.13.201/index")

    time.sleep(15)
    #点击左侧导航栏->系统管理
    xpath('//*[@id="side-menu"]/li[3]/a/span[1]').click()
    time.sleep(5)
    #点击左侧导航栏，系统管理次级菜单->岗位管理
    xpath('//*[@id="side-menu"]/li[3]/ul/li[5]/a').click()
    time.sleep(2)
    #点击新增超链接
    #切换driver到iframe，因为新增超链接是在iframe内。
    driver.switch_to.frame("iframe6")
    time.sleep(2)
    xpath('//*[@id="toolbar"]/a[1]').click()
    time.sleep(2)
    #首先返回到主页，释放iframe
    driver.switch_to.default_content()
    #再次进入另外的新的iframe
    driver.switch_to.frame("layui-layer-iframe1")
    #在添加岗位页面，输入岗位名称
    name('postName').send_keys(postName)

    #在添加岗位页面，输入岗位编码
    name('postCode').send_keys(postCode)
    #在添加岗位页面，输入显示顺序
    name('postSort').send_keys('1')

    #在添加岗位页面，输入备注
    name('remark').send_keys("remark text 1")

    #首先返回到主页，释放iframe
    time.sleep(3)
    driver.switch_to.default_content()

    #在添加岗位页面，点击确定按钮
    xpath('//*[@id="layui-layer1"]/div[3]/a[1]').click()
    time.sleep(5)
