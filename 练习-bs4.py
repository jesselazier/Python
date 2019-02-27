

from bs4 import BeautifulSoup

myhtml=''''''

mysoup=BeautifulSoup(myhtml,'html.parser')

myh1=mysoup.findAll('h1')

for i in myh1:
    if 'jesse' in i.string:
      print(i.string)