__author__ = 'Administrator'
import urllib.request
from bs4 import BeautifulSoup

response = urllib.request.urlopen("http://www.cnitpm.com/st/5620.html")

str = response.read().decode("utf-8")

soup = BeautifulSoup(str, "html.parser")
print(soup.select("div.haf_list"))

# 获取评论地址
# print("http://www.cnitpm.com" + soup.select("span.rmbt + a")[0].get("href"))