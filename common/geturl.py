def GetUrl(url):
    urls=url.split('/')
    url=urls[0]+'/'+urls[1]+'/'+urls[2]+'/'
    return url
testurl=GetUrl('https://www.baidu.com/')
print(testurl)