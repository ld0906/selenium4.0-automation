from Chapter11.Base.base_update import  Base
from selenium.webdriver.common.by import  By
import time
class IndexPage(Base):
    def index_sysadmin(self):
        return self.findele(By.XPATH,'//*[@id="side-menu"]/li[3]/a/span[1]')
    
    def index_postadmin(self):
        return self.findele(By.XPATH,'//*[@id="side-menu"]/li[3]/ul/li[5]/a')

