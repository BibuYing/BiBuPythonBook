import json

# 将一个列表通过json格式存储到文件中
numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

# 读取json文件
with open(filename) as f_obj:
    numbers = json.load(f_obj)
    print(numbers)

# 存储json对象
data = {"name": "Bibu", "num": [1, 2, 3, 4, 5, 6, 7, 8, 9]}
filename2 = 'data.json'
with open(filename2, 'w') as f_obj:
    json.dump(data, f_obj)

# 解析json对象
with open(filename2) as f_obj:
    d = json.load(f_obj)
    print(d)
    print(d["name"])
    print(d["num"][0])
