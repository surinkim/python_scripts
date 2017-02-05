from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def getLinks(url, expression):
    html = urlopen("http://legacy.python.org" + url)
    bsObj = BeautifulSoup(html, "html.parser")
    return bsObj.findAll("a", href = re.compile(expression))

## first
firstUrl = "/download/releases/"
firstExpression = "binaries.*"

secondUrl = firstUrl
secondExpression = "linux.*"

links = getLinks(firstUrl, firstExpression)
for link in links:
    if 'href' in link.attrs:
        print("===================================================")
        print(link.attrs['href'])
        links2 = getLinks(secondUrl + link.attrs['href'], secondExpression)
        for link2 in links2:
            print(link2.attrs['href'])
            
