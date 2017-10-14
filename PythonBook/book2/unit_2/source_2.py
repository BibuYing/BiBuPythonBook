from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "lxml")

# 抓取网页中人名
# 获取表情名为class 并且class=green
nameList = bsObj.findAll("span", {"class": "green"})

for name in nameList:
    # 获取表情内容
    print(name.get_text())

# 获取第一个h1的文本
bsObj.h1.get_text()

# 获取多个属性
nameList = bsObj.findAll("span", {"class": {"green", "red"}})

# 获取class为gerrn的所有标签
nameList = bsObj.findAll(class_="green")
nameList = bsObj.findAll("", {"class": "green"})

# 内容包含了 "the prince"的标签
nameList = bsObj.findAll(text="the prince")