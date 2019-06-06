#get the libraries we need
import nltk
from bs4 import BeautifulSoup
from urllib import request
import ssl
imo
context = ssl._create_unverified_context()
#store the url
url = "http://gitub.com/humanitiesprogramming/scraping-corpus"
html = request.urlopen(url).read()
soup = BeautifulSoup(html, 'lxml')
print(soup.text)

# soup = BeautifulSoup(html, 'lxml')
# our_text = soup.text
# links = soup.find_all('a')[0:10]
#
# links_html = soup.select('td.content a')
#
# urls = []
# for link in links_html:
#     to_append = link['href'].replace('blob/', '')
#     urls.append("https://raw.githubusercontent.com" + to_append)
#
# print(urls)


for saint in saints:
    for city in cities:
        print(saint + city)
