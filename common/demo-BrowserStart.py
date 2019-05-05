from common.readconfig import *
from selenium import webdriver
from common.cappic import CapPic
import os
def BrowserStart():
    browsername = getbrowsername('chrome')
    url = geturl('jc01_core')
    if browsername=='firefox':
        driver = webdriver.Firefox()
        driver.get(url)
    if browsername=='chrome':
        driver = webdriver.Chrome()
        driver.get(url)
    CapPic(driver)
BrowserStart()
