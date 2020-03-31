from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from random import choice
import re


browser = webdriver.Chrome() # 打开谷歌浏览器
wait = ui.WebDriverWait(browser,10)

browser.get("http://s.weibo.com/")