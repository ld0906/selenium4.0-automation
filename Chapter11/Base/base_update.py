from Chapter11.Common.log import FrameLog
from selenium import webdriver
#对base代码进行优化、增加
class Base():
    def __init__(self,driver):
        self.driver = driver
        self.log =FrameLog().log()

   # 单星号参数代表此处接受任意多个非关键字参数
    def findele(self,*args):
        try:
            print(args)
            self.log.info("通过"+args[0]+"定位,元素是"+args[1])
            return  self.driver.find_element(*args)
        except:
            #在页面上没有定位到相应的元素。
            self.log.error("定位元素失败！")
    #对元素click
    def click(self,args):
        self.findele(args).click()
    #输入值
    def sendkey(self,args,value):
        self.findele(args).send_keys(value)
    #调用js方法
    def js(self,str):
        self.driver.execute_script(str)

    def url(self):
        return  self.driver.current_url

    # 后退
    def back(self):
        self.driver.back()
    #前进
    def forword(self):
        self.driver.forward()
    #退出
    def quit(self):
        self.driver.quit()
    
    #切换到iframe，在点击“新增”岗位信息按钮前调用
    def go_frame_1(self):
        self.driver.switch_to.frame("iframe6")

    #切换到主页函数，在需要切换到主页时调用
    def go_content(self):
        self.driver.switch_to.default_content()

    #切换到iframe，在输入岗位名称前调用
    def go_frame_2(self):
        self.driver.switch_to.frame("layui-layer-iframe1")

