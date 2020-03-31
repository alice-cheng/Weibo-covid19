import bs4, sys
from bs4 import BeautifulSoup, NavigableString, Tag

from pprint import pprint
with open('results.html', 'r', encoding='utf-8') as f:
    webpage = f.read()

soup = bs4.BeautifulSoup(webpage, features="html.parser")
results = soup.find_all('div',  attrs={"node-type": "feed_list_forwardContent"})
cards = []


posts = []
for card in results:
    
    res = card.find('a', href='https://huati.weibo.com/6882551')
    if not res:
        txt = card.find('p',attrs={"class":'txt'})
        brs = txt.find_all('br')
       
        posts.append(card)

# pprint(posts)
pprint(len(posts))

