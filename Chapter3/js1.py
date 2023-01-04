from selenium import webdriver
from selenium.webdriver.chrome.service import Service

#这是在mac上执行的基于chrome浏览器上的测试，如下driver地址请根据实际情况进行修改。
chrome_driver_server = Service("/Users/jason118/Downloads/chromedriver")
driver  = webdriver.Chrome(service=chrome_driver_server)
driver.get("https://sogou.com")


query = '''
         // 注意 Javascript代码的注释符号不是#,
         //利用DOM的getElementById方法获取搜索输入框元素。
         var keyinput1 = document.getElementById("query");
         //为输入框元素，设置值，如'Python'
         keyinput1 = "Python";
          setTimeout(function(){
         //利用DOM的getElementById方法获取搜索按钮。
         var button1 = document.getElementById("stb");
         button1.click();

         },4000);
         '''
driver.execute_script('document.getElementById("query").value ="Python"')
driver.execute_script('document.getElementById("stb").click()')

