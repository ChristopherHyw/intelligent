import requests
from pyquery import PyQuery as pq
from selenium import webdriver

# url = 'https://detail.tmall.com/item.htm?spm=a230r.1.14.6.39343c05sgLWEg&id=551813803016&cm_id=140105335569ed55e27b&abbucket=12'
url = 'https://www.taobao.com'

# html = requests.get(url).text
from selenium import webdriver
browser = webdriver.Chrome()
browser.get(url)
html = browser.page_source
print(html)
browser.close()

# result_dir = 'D:/WorkSpace/PyCharm/intelligent/com/datas/crawler_data/taobao1.txt'
#
# with open(result_dir, 'a', encoding='utf-8') as file:
#     file.write(html)
#
# doc = pq(html)
# items = doc('.explore-tab .feed-item').items()
# for item in items:
#     question = item.find('h2').text()
#     author = item.find('.author-link-line').text()
#     answer = pq(item.find('.content').html()).text()
#
#     result_dir = 'D:/WorkSpace/PyCharm/intelligent/com/datas/crawler_data/zhihu_question.txt'
#
#     with open(result_dir,'a',encoding='utf-8') as file:
#
#         file.write('\n'.join([question,author,answer]))
#         file.write('\n'+'='*50+'\n')