from bs4 import BeautifulSoup
import urllib.request

fp = urllib.request.urlopen("https://google.com")
mybytes = fp.read()
mystr = mybytes.decode("utf8")
fp.close()

soup = BeautifulSoup(mystr, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))
