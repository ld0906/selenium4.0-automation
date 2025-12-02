import yaml
file_1 = open('config.yml')
#返回一个字典对象
yml = yaml.load(file_1,Loader=yaml.FullLoader)
print(yml)
print(type(yml))