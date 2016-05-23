import urlparse
import urllib
from bs4 import BeautifulSoup

url = "https://uk.yahoo.com/"

urls = [url]
visited = [url]

def crawler():
    for url in urls:
        print "Crawling: " + url
        try:
            htmltext = urllib.urlopen(urls[0]).read()
        except:
                print urls[0]
        soup = BeautifulSoup(htmltext, "html.parser")

        urls.pop(0)
        visited.append(url)

        for tag in soup.findAll('a',href=True):
            tag['href'] = urlparse.urljoin(url,tag['href'])
            urls.append(tag['href'])
            print tag['href']
        
def start():
    while len(urls) >0:
        try:
            htmltext = urllib.urlopen(urls[0]).read()
        except:
                print urls[0]
        soup = BeautifulSoup(htmltext)

        urls.pop(0)
        visited.append(url)

        for tag in soup.findAll('a',href=True):
            tag['href'] = urlparse.urljoin(url,tag['href'])
            urls.append(tag['href'])
            print tag['href']
start()
while 1:
    crawler()
