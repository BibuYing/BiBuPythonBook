# 打开文件
with open('pi_digits.txt') as file_object:
    # 打印文件内容
    contents = file_object.read()
    print(contents)

filename = 'pi_digits.txt'
with open(filename) as fil_object:
    # 逐行打印
    for line in fil_object:
        print(line)

filename = 'pi_digits.txt'
with open(filename) as file_object:
    # 将文件各行存放在一个列表中
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip() + "---")
