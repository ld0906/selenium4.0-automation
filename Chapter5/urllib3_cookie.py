from urllib import request
import http.cookiejar
import urllib3
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
#disable_warnings()可以消除SSL警告的信息
urllib3.disable_warnings()

#创建CookieJar对象
cookie1 = http.cookiejar.CookieJar()

opener1 = request.build_opener(request.HTTPCookieProcessor(cookie1))

#在打开URL的过程中，会将cookie的信息放入到cookie对象(cookie1)中。
req1 = opener1.open('http://sogou.com')

#遍历cookie对象
for i in cookie1:
    print(i.name + ":"+ i.value)
