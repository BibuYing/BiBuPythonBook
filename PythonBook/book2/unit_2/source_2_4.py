# 正则
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html, "lxml")
# 通过正则表达式，筛选符合条件的标签
images = bsObj.findAll("img", {"src": re.compile("\.\.\/img\/gifts/img.*\.jpg")})
for image in images:
    # 获取src属性
    print(image["src"])
    print(image.attrs["src"])
