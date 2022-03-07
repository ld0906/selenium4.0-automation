from Base.base_update import  Base
from selenium.webdriver.common.by import By
import  time
import fateadm_api 

class LoginPage(Base):

    #以下为登录页面的4个元素定位语句。
    def login_user(self):
        return self.findele(By.NAME,"username")
    
    def login_password(self):
        return self.findele(By.NAME,"password")
    
    def login_validateCode(self):
        return self.findele(By.NAME,"validateCode")
    
    def login_button(self):
        return self.findele(By.ID,"btnSubmit")

    #以下为登录系统的函数。
    def login_system(self,username,password):
        self.login_user().send_keys(username)
        time.sleep(2)
        self.login_password().send_keys(password)
        time.sleep(2)
        verification_code = str(fateadm_api.TestFunc())
        self.login_validateCode().send_keys(verification_code)
        time.sleep(2)
        self.login_button().click()
        return self.url()        

    


