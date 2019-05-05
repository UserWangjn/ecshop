import configparser
import os
def getbrowsername(name):
    cf = configparser.ConfigParser()
    cfpath=os.path.dirname(os.path.abspath('.'))+'/config/config.ini'
    cf.read(cfpath)
    browsername = cf.get('browser',name)
    return browsername
def geturl(url):
    cf = configparser.ConfigParser()
    cfpath=os.path.dirname(os.path.abspath('.'))+'/config/config.ini'
    cf.read(cfpath)
    urlpath = cf.get('browser',url)
    return urlpath
#print(getbrowsername('chrome'))
#print(geturl('jc01_core'))