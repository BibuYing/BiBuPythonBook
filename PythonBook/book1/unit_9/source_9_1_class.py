class Dog():
    """一次模拟小狗的简单尝试"""

    # 每当初始化实例时，就会自动调用此方法
    # 每个与类相关联的方法调用都自动传递实参self ，它是一个指向实例本身的引用，让实例能够访问类中的属性和方法。
    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print(self.name.title() + " rolled over!")


# 根据类创建实例
my_dog = Dog('willie', 6)
#访问类中的属性
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
#调用类中的方法
my_dog.sit()
