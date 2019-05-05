from common.readconfig import *
from selenium import webdriver
from common.cappic import CapPic
from common.loggen import LogGen
import os
logger = LogGen(logger='浏览器启动加载').getlog()
def BrowserStart():
    browsername = getbrowsername('chrome')
    url = geturl('jc01_core')
    if browsername=='firefox':
        driver = webdriver.Firefox()
        driver.get(url)
    if browsername=='chrome':
        logger.info('启动Chrome浏览器')
        driver = webdriver.Chrome()
        logger.info('打开测试网页')
        driver.get(url)
    CapPic(driver)
BrowserStart()
