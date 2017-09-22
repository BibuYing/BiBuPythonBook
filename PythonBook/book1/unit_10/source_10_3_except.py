try:
    print(5 / 0)
except ZeroDivisionError:  # 异常执行
    print("除数不能为0")
else:  # try运行之后，不会异常则执行else
    print("不会抛异常")
finally:  # 不管是否异常，都执行fianlly
    print("最后一步")
