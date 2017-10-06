from bs4 import BeautifulSoup
import urllib.request
f = urllib.request.urlopen("http://www.10jqka.com.cn/")
t = f.read()
s = BeautifulSoup(t)
print(s.prettify()) #格式化输出