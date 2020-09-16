import bs4, sys
import os
from bs4 import BeautifulSoup, NavigableString, Tag

from pprint import pprint

filenames = ['result20200412(1).html','result20200412.html',
             'results.html','results20200421.html',
             'results20200422(3).html','results20200424.html',
             'results20200426(3).html','results20200429(2).html',
             'results20200429.html']

def scrap(file):
    with open(file, 'r', encoding='utf-8') as f:
        webpage = f.read()

    soup = bs4.BeautifulSoup(webpage, features="html.parser")
    # results = soup.find_all('div',  attrs={"node-type": "feed_list_forwardContent"})
    results = soup.find_all('div', {'class': "WB_detail"})
    cards = []

    posts = {}
    i = 0
    for card in results:
        i += 1
        date_line = card.find('a', {'class': 'S_txt2'}).attrs
        date = date_line['title']
        # print(date)
        if date:
            if date in posts:
                posts[date].append([])
            else:
                posts[date] = []
        # print('in' + str(i))
        res = card.find('a', attrs={"node-type": "feed_list_content"})
        # seen = set(posts[date])
        # print('res is: ')
        # print(res)
        # res is None]
        if not res:
            # i += 1
            # print('in' + str(i))
            txt = card.find('a', attrs={"action-type": "feed_list_url"})
            # print('txt line is '+ str(i) + 'of type' + str(type(txt)))
            # print(txt)
            if txt:
                print('in txt')
                brs = txt.find_all('br')
            posts[date].append(card)

        # print(type(card))
    p = 1

    def get_text(element_tag):
        '''(bs4.element.tag) ->(str)
        this function takes a tag and return text content of this tag
        '''
        content = []
        for sub_ele in element_tag:
            # print('sub_ele is: ')
            # print(type(sub_ele))
            # print(sub_ele)
            if type(sub_ele) == bs4.element.NavigableString:
                if sub_ele:
                    # print('non empty navigstring is: ')
                    navi = str(sub_ele).strip()
                    if navi:
                        # print('navi is: ')
                        content.append(navi)
        return ''.join(content).split()

    refined = {}
    for date in posts:
        refined[date] = []
        # print(str(p))
        # pprint(date)
        # print('type of post is: ')
        # print(type(posts[date]))
        #
        # print('length of list is: ')
        # print(len(posts[date]))
        for sub_post in posts[date]:
            # print('type of sub_post is: ')
            # print(type(sub_post))
            # pprint(sub_post)
            for ele in sub_post:
                if type(ele) == bs4.element.Tag:
                    # send to function to extract text
                    # print('found tag/ele')
                    # print(ele)
                    # print('tag type: ')
                    # print(type(ele))
                    # print('get_text give you: ')
                    if ele != None:
                        refined[date].append(get_text(ele))

        # pprint(posts[post])
        p += 1

    # pprint(len(posts))

    # pprint(refined)

    import csv

    fields = []
    row = []
    for date in refined:
        fields.append(date)
        print(date)
        # print(refined[date])
        content = refined[date]
        # flatten list of lists
        flattened = [sub_ele for ele in content for sub_ele in ele]
        # remove duplicates
        res = [i for n, i in enumerate(flattened) if i not in flattened[:n]]
        # print(type(res))
        # print(res)
        row_ele = "".join(res)
        # row_ele = (row_ele.encode('ascii', 'ignore')).decode("utf-8")
        # print(row_ele)
        row_ele = row_ele.replace('\u200b', '').strip()
        row.append(row_ele)
        # print(row)

    print('length of fields')
    print(len(fields))

    print('length of row')
    print(len(row))
    pprint(row)

    import pandas as pd
    data = {'timestamp': fields, 'post': row}
    df = pd.DataFrame(data)
    pprint(df)
    print(type(df))


    if not os.path.isfile('C:/Users/Alice/Desktop/project/results.csv'):
        df.to_csv('results.csv', header='column_names')
    else:
        df.to_csv('results.csv', mode = 'a', header = False)
    # save_path = 'C:/Users/Alice/Desktop/project/results.csv'
    # df.to_csv(save_path, mode = 'a', header = save_path.tell()==0)
for file in filenames:
    scrap(file)