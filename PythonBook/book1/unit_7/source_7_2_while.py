# while循环

# 你可以使用while 循环来数数，例如，下面的while 循环从1数到5
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

print("------------------")
# break 退出循环
postion = 0;
while postion < 10:
    if postion > 5:
        break

    postion += 1
    print(postion)
print("------------------")

# continue 跳出本次循环
postion2 = 0
while postion2 < 10:
    postion2 += 1
    if postion2 % 2 == 0:
        continue
    print(postion2)

# 删除列表中所有元素

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
