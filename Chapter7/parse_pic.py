import easyocr

# 创建reader实例,由于验证码都是英文字母，所以如下的reader只选择了英语这一种语言。
reader1 = easyocr.Reader(['en','ch_sim'])

text = reader1.readtext("/Users/jason118/PycharmProjects/selenium4.0-automation/Chapter7/t.jpg")
print(text)