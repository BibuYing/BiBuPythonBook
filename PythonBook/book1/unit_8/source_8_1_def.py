# 函数
def greet_user():
    """显示简单的问候语"""
    print("Hello!")


greet_user()


# 传递实参
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


# 位置实参
describe_pet('hamster', 'harry')

# 关键字实参
describe_pet(animal_type='hamster', pet_name='harry')


# 默认值
def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


# 调用带默认值方法
describe_pet(pet_name='willie')


# 传递任意数量的实参
# 形参名*toppings 中的星号让Python创建一个名为toppings 的空元组，
# 并将收到的所有值都封装到这个元组中。
def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# 任意数量关键字参数
def getuser(**user_info):
    for key, value in user_info.items():
        print(key + "---" + value)
    if user_info['name']:
        print("Hello," + user_info['name'])


getuser(name='bibu', age='25')

# 函数的参数为列表的话，会对实际列表进行操作
a = [1, 2, 3, 4, 5]
print(a)


def ppp(aa):
    aa.pop()


# 列表被传入函数后，被移除最后一个
ppp(a)
print(a)
# 切片表示法，使用切片，传入一个新的函数
ppp(a[:])
print(a)
