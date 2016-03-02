from urllib.request import urlopen
textPage = urlopen(
"http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")
s=(str(textPage.read(), 'utf-8'))#如果print会失败，但是交互式显式a是成功的
#print(s)#只可以print a，如果textPage.read是不行的，它已经被读过了，空了
s2= s.encode("gbk",errors="ignore").decode('gbk')
print('now is chinese: \n',s2)