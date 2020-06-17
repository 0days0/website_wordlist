import requests 
from bs4 import BeautifulSoup

adres = input('Url: ')
istek = requests.get(adres)
html = istek.content

soup = BeautifulSoup(html, 'html.parser')
soup = soup.find_all('p') # p taglerini alır
#print(soup)
file = open('wordlist.txt', 'w') # bulunduğu dizinde wordlist.txt belgesini oluşturur
for i in soup:
    One = str(i.text)
    One = One.split() # kelimeleri boşluklardan ayıracaktır  
    for s in One:
       file.write(s + '\n')
file.close()
print('Wordlist oluşturuldu..!') 