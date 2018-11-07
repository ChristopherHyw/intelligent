from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote

browser = webdriver.Chrome()
wait = WebDriverWait(browser,60)
KEYWORD = 'iPad'

from pyquery import PyQuery as pq
def get_products():
    """
    提取商品数据
    :return:
    """
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image':item.find('.pic .img').attr('data-src'),
            'price':item.find('.price').text(),
            'deal':item.find('deal-cnt').text(),
            'title':item.find('.title').text(),
            'shop':item.find('.shop').text(),
            'location':item.find('.location').text()
        }
        print(product)
        result_dir = 'D:/WorkSpace/PyCharm/intelligent/com/datas/crawler_data/taobao_product.txt'
        file = open(result_dir,'a',encoding='utf-8')
        file.write(str(product))
        file.close()


def index_page(page):
    """
    抓取索引页
    :param page: 页码
    :return:
    """
    print('正在爬取',page,'页')
    try:
        url = 'https://s.taobao.com/search?q='+quote(KEYWORD)
        print("-------------------------------------------------------")
        print(url)
        browser.get(url)
        if page > 1:
            input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#mainsrp-pager div.from > input.input.J_Input')))
            submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#mainsrp-pager div.from > span.btn.J_Submit')))
            input.clear()
            input.send_keys(page)
            submit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,'#mainsrp-pager li.item.active > span'),str(page)))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'.m-itemlist .items .item')))
        get_products()
    except TimeoutException:
        index_page(page)

MAX_PAGE = 4
def main():
    """
    遍历每一页
    :return:
    """
    for i in range(1,MAX_PAGE+1):
        index_page(i)

if __name__ == '__main__':
    main()