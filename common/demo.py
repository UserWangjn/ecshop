import time
import os
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.baidu.com')
pt=time.strftime('%Y%m%d%H%M',time.localtime())
#print(pt)
picname = os.path.dirname(os.path.abspath('.'))+'/picture/'+pt+'.png'
#print(picname)
driver.get_screenshot_as_file(picname)