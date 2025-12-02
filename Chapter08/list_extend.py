list_1 = [3,6,9,"selenium","8.9093",["a","B","C","abc"]]
print("append添加列表元素之前，遍历列表元素，并打印")
for l in list_1: #for循环遍历所有的列表元素，并打印
    print(l)
list_1.extend(['e','f','g'])
print("\n") #换行操作
print("append添加列表元素之后，遍历列表元素，并打印")
for l in list_1: #for循环遍历所有的列表元素，并打印
    print(l)