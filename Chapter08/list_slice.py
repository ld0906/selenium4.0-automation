list_1 = [3,6,9,"selenium","8.9093","-9"]
print("列表分片之前，遍历列表元素，并打印")
for l in list_1: #for循环遍历所有的列表元素，并打印
    print(l)

print("\n") #换行操作
temp = list_1[3] #返回的是一个字符串，是列表中的第4个元素。
print(temp)

temp = list_1[2:4] #连续分片，返回的是一个新的列表temp,列表元素为老列表的第3，4个元素组成。
print(temp)
print("列表分片之后，遍历列表元素，并打印")
for l in list_1: #for循环遍历所有的列表元素，并打印
    print(l)
