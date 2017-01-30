from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://legacy.python.org/download/releases/binaries-1.5/")
bsObj = BeautifulSoup(html, "html.parser")

##모든 href 검색
#for link in bsObj.findAll("a"):
#    if 'href' in link.attrs:
#        print(link.attrs['href'])

##python으로 시작하는 href만 검색
#for link in bsObj.findAll("a", href = re.compile("^(python).*$")):
#    if 'href' in link.attrs:
#        print(link.attrs['href'])

## ?C=N;O=D, /download/releases/ 와 같이 ?, / 를 제외하고 검색
for link in bsObj.findAll("a", href = re.compile("^((?![?/]).)*$")):
    if 'href' in link.attrs:
        print(link.attrs['href'])