"""
Created on Tue Apr 01 11:21:29 2014
@author: tanhe
"""
from functools import reduce

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import selenium.webdriver.support.ui as ui
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from random import choice
import re

# import pickle
# driver = webdriver.Chrome(ChromeDriverManager().install())

browser = webdriver.Chrome()  # 打开谷歌浏览器
wait = ui.WebDriverWait(browser, 10)
# browser.set_page_load_timeout(1000)
browser.get("http://s.weibo.com/")


def login():
    wait.until(lambda browser: browser.find_element_by_xpath("//a[@node-type='loginBtn']"))
    browser.find_element_by_xpath("//a[@node-type='loginBtn']").click()
    print('waiting...')
    # n = 15

    sleep(10)
    wait.until(lambda browser: browser.find_element_by_xpath("//a[@node-type='qrcode_tab']"))
    browser.find_element_by_xpath("//a[@node-type='qrcode_tab']").click()
    # user.clear()
    # user.send_keys(username)
    # psw = browser.find_element_by_xpath("//input[@name='password']")
    # psw.clear()
    # psw.send_keys(password)
    # browser.find_element_by_xpath("//div[6]/a/span").click()
    # position: fixed; top: 0px; left: 0px; width: 953px; height: 925px; background: rgb(0, 0, 0); opacity: 0.3; z-index: 9999;
    # wait.until(lambda browser: browser.find_element_by_xpath("//a[@node-type='loginBtn']"))
    sleep(15)
    wait.until(lambda browser: browser.find_element_by_xpath("//a[@class='gn_name']"))


##登陆完成，若出现用户名，则开始进行搜索
def search(searchWord):
    wait.until(lambda browser: browser.find_element_by_class_name("searchbox"))
    inputBtn = browser.find_element(By.XPATH, '//input')
    print(inputBtn)

    inputBtn.send_keys(searchWord)

    # browser.find_element(By.XPATH, '//button[class="s-btn-b"]').click()
    browser.find_element_by_class_name('s-btn-b').click()

    # wait.until(lambda browser: browser.find_element_by_class_name("search_num"))


# texts = browser.find_elements_by_xpath("//dl[@class='feed_list W_linecolor ']/dd[@class='content']/p[@node-type='feed_list_content']/em")
def gettext():
    content = []
    wait.until(lambda browser: browser.find_element_by_xpath("//div[@class='m-error']/a"))
    feed_list_items = browser.find_elements_by_xpath("//div[@action-type='feed_list_item']")
    print(feed_list_items)
    for item in feed_list_items:
        print(item.get_attribute('innerHTML'))
    # with open('results.html', 'wb+') as f:
    #     for item in feed_list_items:
    #         f.write(item.get_attribute('innerHTML'))
    print('trying to get more results...')
    browser.find_element_by_xpath("//div[@class='m-error']/a").click()
    link_list = browser.find_element_by_xpath("//ul[@class='s-scroll']")

    # print len(texts)
    # print(feed_list_items)
    # with open('results.html', 'w+') as f:
    #     for item in feed_list_items:
    #         f.write(item)
    # for n in texts:
    #     try:
    #         highpoints = re.compile(u'[\U00010000-\U0010ffff]')
    #     except re.error:
    #         highpoints = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')
    #         mytext =  highpoints.sub(u'', n.text)
    #         print (mytext.encode("gbk"))
    #         content.append(mytext.encode("utf-8"))
    return content


def nextPage():
    # wait.until(lambda browser: browser.find_element_by_class_name("search_page_M"))
    if browser.find_elements_by_xpath("//ul[@class='search_page_M']") != None:
        nums = len(browser.find_elements_by_xpath("//ul[@class='search_page_M']/li"))
        # browser.execute_script("window.scrollTo(0, 7100)")
        pg = browser.find_element_by_xpath("//ul[@class='search_page_M']/li[%d]/a" % nums)  # .text.encode("gbk")
        y = pg.location['y'] + 100
        print(y)
        browser.execute_script('window.scrollTo(0, {0})'.format(y))
        ActionChains(browser).move_to_element(pg).click(pg).perform()

def splitkeepsep(pages, sep):
    return reduce(lambda acc, elem: acc[:-1] + [acc[-1] + elem] if elem == sep else acc + [elem], re.split("(https://)",(page for page in pages)), [])

def main():
    login()
    # super index has 23 pages
    # click nextpage for 22 times
    i = 1
    base_url = 'https://www.weibo.com/p/1008084882401a015244a2ab18ee43f7772d6f/super_index?pids=Pl_Core_MixedFeed__261&current_page=3&since_id=4483390936041792&page=1#Pl_Core_MixedFeed__261'

    f = open('results20200421', 'a' , encoding = 'utf-8')
    for i in range(1,23):
        current_url = base_url[:-24] + str(i) + base_url[-23:]
        browser.get(current_url)
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        feed_list_items = browser.find_elements_by_xpath("//div[@action-type='feed_list_item']")
        for item in feed_list_items:
            f.write(item.get_attribute('innerHTML'))
        # wait.until(lambda browser: browser.find_element_by_xpath("//a[@bpfilter='page']"))
        # if browser.find_element_by_xpath("//a[@bpfilter='page']").click():
        #     print('going to page ' + str(i + 1) + ' ...')
        # else:
        #     print('could not find next page btn')
        i += 1
        sleep(7)
    f.close()
main()