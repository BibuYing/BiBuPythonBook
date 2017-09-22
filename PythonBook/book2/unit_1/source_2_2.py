# 导航树
# 抓取购物网站http://www.pythonscraping.com/pages/page3.html


from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "lxml")
# 打印子标签
# for child in bsObj.find("table", {"id": "giftList"}).children:
#     print(child)

# 打印后代所有标签
# for child in bsObj.find("table", {"id": "giftList"}).descendants:
#     print(child)

# 打印除了第一行之外的所有兄弟标签
# for sibling in bsObj.find("table", {"id": "giftList"}).tr.next_siblings:
#     print(sibling)

# 获取img标签的父类标签的上一个兄弟标签
print(bsObj.find("img", {"src": "../img/gifts/img1.jpg"
                         }).parent.previous_sibling.get_text())
