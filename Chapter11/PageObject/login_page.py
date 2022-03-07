from Chapter11.Base.base_update import  Base
from selenium.webdriver.common.by import By
import  time,os
from Chapter11.PageObject import fateadm_api 


class LoginPage(Base):

    #以下为登录页面的4个元素定位语句。
    def login_user(self):
        return self.findele(By.NAME,"username")
    
    def login_password(self):
        return self.findele(By.NAME,"password")
    
    def login_validateCode(self):
        return self.findele(By.NAME,"validateCode")
    
    def login_validateImage(self):
        return self.findele(By.XPATH,'//*[@id="signupForm"]/div[1]/div[2]/a/img')
    
    def login_button(self):
        return self.findele(By.ID,"btnSubmit")
    

    #以下为登录系统的函数。
    def login_system(self,username,password):
        filename = "capture.png"
        if os.path.exists(filename):
            os.remove(filename)
        self.login_validateImage().screenshot(filename)
        
        self.login_user().clear()
        self.login_user().send_keys(username)
        time.sleep(2)
        self.login_password().clear()
        self.login_password().send_keys(password)
        time.sleep(2)
        verification_code = str(fateadm_api.TestFunc())
        self.login_validateCode().send_keys(verification_code)
        time.sleep(2)
        self.login_button().click()
        return self.url()        

