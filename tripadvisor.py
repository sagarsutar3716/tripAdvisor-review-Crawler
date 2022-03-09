import requests
from bs4 import BeautifulSoup as soup
from random import randint
from time import sleep
from xlwt import *

workbook = Workbook(encoding = 'utf-8')
table = workbook.add_sheet('data')
table.write(0, 0, 'Number')
table.write(0, 1, 'review_url')
table.write(0, 2, 'Review')
line = 1

url = requests.get('https://www.tripadvisor.in/Hotels-g187147-Paris_Ile_de_France-Hotels.html')
url.status_code
sop = soup(url.content,'lxml')

links=[]
num = 0

for review in sop.find_all('a',{'class':'review_count'}):
    a = review['href']
    a = 'https://www.tripadvisor.in'+a
    print(a)
    print(a.find('Reviews'))
    a = a[:(a.find('Reviews')+3)] + '-or{}' + a[(a.find('Reviews')+3):]
    print(a)
    links.append(a)
num += 1
links


reviews = []
for link in links:
    d = [5]  # [5,10,15,20] if need more data (one page shows 5 reviews)
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
    }
    secnd_url = requests.get(link.format(i for i in d),headers=headers)
    sleep(randint(1,5))
    a_sop = soup(secnd_url.content,'lxml')
    for r in a_sop.find_all('q'):
        reviews.append(r.span.text.strip())
        print(r.span.text.strip())
table.write(line, 0, num)
table.write(line, 1, a)
table.write(line, 2, r.span.text.strip()())
line += 1
reviews
workbook.save('Review.xls')



