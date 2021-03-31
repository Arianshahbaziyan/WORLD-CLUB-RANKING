import re
import requests
from bs4 import BeautifulSoup

s=0
shomaresh=0
asami=list()
ranking=list()
points=list()

for i in range(1,4):
    s=i
    data=requests.get('https://footballdatabase.com/ranking/world/%i'%(s))
    soup=BeautifulSoup(data.text,'html.parser')
    val=str(soup.find_all('div',attrs={'itemprop':'itemListElement'}))
    valr=str(soup.find_all('td'))
    rank=re.findall(r' <td class="rank">(.*?)</td>',valr)
    name=re.findall(r'itemprop="itemListElement">(.*?)</div>',val)

    for r in range(0,len(rank)):
        if r % 2 == 0:
         ranking.append(rank[r])
    
    for ii in range(0,len(name)):
        asami.append(name[ii])
        points.append(ranking[ii])

esm=''
nomre=''
print("\n","World Football / Soccer Clubs Ranking","\n","Updated after matches played on 28 March 2021","\n")
for ix in range(0,len(asami)):
    esm=asami[ix]
    nomre=points[ix]
    shomaresh=ix+1
    print("%i -  %s | points:  ( %s ) "%(shomaresh,esm,nomre))
    print("___________________________________________________")