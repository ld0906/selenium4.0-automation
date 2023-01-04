import json
f = open("ttt.json","w")
js = {'android1': 'appium', 'web1': 'selenium', 'interface1': 'python interface automation'}
json.dump(js,f)
