from Base.base_update import  Base
from selenium.webdriver.common.by import  By
import  time
class AddPositionPage(Base):
    
    #定位‘新增’HTML超链接元素
    def add_position_insert(self):
        return self.findele(By.XPATH,'//*[@id="toolbar"]/a[1]')
    
    #定位岗位名称输入框
    def add_position_name(self):
        return self.findele(By.NAME,'postName')
    
    #定位岗位编码输入框
    def add_position_code(self):
        return self.findele(By.NAME,'postCode')
    
    #定位显示顺序输入框
    def add_position_order(self):
        return self.findele(By.NAME,'postSort')
    
    #定位备注多行文本输入框
    def add_position_remark(self):
        return self.findele(By.NAME,'remark')
    
    #定位确定超链接
    def add_position_confirm(self):
        return self.findele(By.XPATH,'//*[@id="layui-layer1"]/div[3]/a[1]')
    

    #添加岗位信息方法，输入参数为岗位名称和岗位编码
    def add_post(self,postName,postCode):
        self.go_frame_1()
        self.add_position_insert().click()
        time.sleep(2)
        self.go_content()
        self.go_frame_2()
        self.add_position_name().send_keys(postName)
        time.sleep(2)
        self.add_position_code().send_keys(postCode)
        time.sleep(2)
        self.add_position_order().send_keys("1")
        time.sleep(2)
        self.add_position_remark().send_keys("remark text 1")
        time.sleep(2)
        self.go_content()
        self.add_position_confirm().click()
        time.sleep(2)
        
