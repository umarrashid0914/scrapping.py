# Parse any Url
# pip install requests
# pip install beautifulsoup4
import requests
from bs4 import BeautifulSoup
dta = requests.get('https://master.d1mu8nw8h8t8ic.amplifyapp.com/')
#print(dta.content)
soap = BeautifulSoup(dta.content,features="html.parser")
#print(soap.html.head.title)
#print(soap.html)
print(soap.find_all('new'))
for a in soap.find_all('new'):
    print (a)

#for d in soap.find_all("div", class_ = "course-title"):
 #   print(d)

