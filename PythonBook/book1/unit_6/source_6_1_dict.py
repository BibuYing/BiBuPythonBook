# 一个简单的字典
alien_0 = {'color': 'green', 'points': 5,'name':'bibu'}
print(alien_0['color'])
print(alien_0['points'])

# 添加键值对
alien_0["x_postion"] = 0
print(alien_0["x_postion"])

# 修改键值对
alien_0["x_postion"] = 1
print(alien_0["x_postion"])

# 删除键值对
print(alien_0)
del alien_0["x_postion"]
print(alien_0)

# 遍历字典
# 要编写用于遍历字典的for 循环，可声明两个变量，用于存储键—值对中的键和值。对于这两个变量，可使用任何名称
for key, value in alien_0.items():
    print(key + "---" + str(value))

# 遍历字典中所有键
for key in alien_0.keys():
    print(key)

# 遍历字典中所有值
for value in alien_0.values():
    print(value)

#判断值是否存在
if 'name' in alien_0.keys():
    print("存在")
else:
    print("不存在")