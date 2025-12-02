list_1 = [3,6,9,"selenium","8.9093","-9"]
print("执行删除列表元素之前，遍历列表元素，并打印")
for l in list_1: #for循环遍历所有的列表元素，并打印
    print(l)
pop_res = list_1.pop() #删除 位置序号为1的元素，也就是列表中第2个元素
print("\n")
print("pop()方法返回的元素："+pop_res)
print("\n") #换行操作
print("执行删除列表元素之后，遍历列表元素，并打印")
for l in list_1: #for循环遍历所有的列表元素，并打印
    print(l)
