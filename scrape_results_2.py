import bs4, sys
from bs4 import BeautifulSoup, NavigableString, Tag

from pprint import pprint
with open('results.html', 'r', encoding='utf-8') as f:
    webpage = f.read()

# create a dictionary of post
# key = date (type str)
# value = content in post(s) posted on date(type list)
post_dict = {}

soup = bs4.BeautifulSoup(webpage, features="html.parser")
# results = soup.find_all('div',  attrs={"node-type": "feed_list_forwardContent"})

# found all weibo posts (each is in one class called "WB-detail")
posts = soup.find_all('div', {'class': "WB_detail"})

# find date in one post
def get_date(s_txt2):
    '''(bs4.element.Tag) -> '''
    # get attributes and put into a dict
    dict_attrs = s_txt2.attrs
    date = dict_attrs['title']
    return date

# loop through each post
for post in posts:
    # print(type(weibo))

    # step1: find timestamp and make it key in post dict
    card_id = post.find('a', {'class':"S_txt2"})
    id = card_id.find('a', {})
    post_date = get_date(card_id)
    print(post_date)
    post_dict[post_date] = []

    # step2: find content of a post and store it as value corresponds to key(type list)
    # find div class where feed_list_content is
    post_content = post.find('div', {'node-type':"feed_list_content"})
    print(post_content)
    # loop through components (NavigableString or Tag) in the class
    # only store patient information (type navigableString)

    # one for loop: break class into components of either navigableString or tag
    # nested for loop (2): break them into string, navigableString or tag
    #   <i class="W_ficon ficon_supertopic"></i> type <class 'bs4.element.Tag'>
    #   息 type <class 'str'>
    #   肺炎患者求助超话 type <class 'bs4.element.navigableString>
    for data in post_content:
        print(data)
        if isinstance(data, bs4.element.NavigableString):
            # print('type naviString')
            post_dict[post_date].append(data)

        # else:
            # print('type of element is: ')

            # print(type(component))
            # print(component)

for data in post_dict:
    print('inpost')

    print(data)
    print(post_dict[data])

# results = soup.find_all('div', {'node-type': "feed_list_content"})
# cards = []



# i=0



