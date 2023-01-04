from login import login
from add_position import add_position
from functions import read_excel
from functions import log


#首先登录系统
log("Begin to log in system.")
login()
log("Log in system done.")

log("fetch position test data from Excel file")
dict1 =  read_excel("position_data.xlsx",0)

log("Begin to add position in system.")
#测试添加岗位信息场景
add_position(dict1[0][0],dict1[0][1])
log("Add position done.")

