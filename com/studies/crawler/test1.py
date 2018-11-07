
#import urllib.request

# response = urllib.request.urlopen('https://www.python.org')

# print(response.read().decode('utf-8'))
# print(type(response))
# print(response.status)
# print(response.getheaders())
# print(response.getheader('Server'))
##################################################################

# import urllib.parse
# import urllib.request
#
# data = bytes(urllib.parse.urlencode({'world':'hello'}),encoding='utf8')
# response = urllib.request.urlopen('http://httpbin.org/',data=data)
# print(response.read())
# response = urllib.request.urlopen('http://httpbin.org/get',data=data,timeout=1)
# print(response.read())
#############################################################################

# import socket
# import urllib.request
# import urllib.error
# try:
#     response = urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
# except urllib.error.URLError as e:
#     if isinstance(e.reason,socket.timeout):
#         print('TIME OUT')

# import http.cookiejar,urllib.request
# cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# for item in cookie:
#     print(item.name+"="+item.value)
#
# import os
# os.path.basename('C:/Program Files (x86)/Google/chromeDriver')
# os.path.basename('C:/Program Files (x86)/Google/Chrome/Application')


# chromedriver = "C:/Program Files (x86)/Google/chromeDriver"
# os.environ["webdriver.chrome.driver"] = chromedriver
# driver = webdriver.Chrome(chromedriver)
# from selenium import webdriver
# browser = webdriver.Chrome('C:/Program Files (x86)/Google/chromeDriver')
# browser = webdriver.Chrome()