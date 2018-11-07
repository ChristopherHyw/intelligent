import requests
from urllib.parse import urlencode

def get_page(offset):
    params = {
        'offset':offset,
        'format':'json',
        'keyword':'街拍',
        'autoload':'true',
        'count':'20',
        'cur_tab':'1',
        'from': 'search_tab'
    }
    url = 'http://www.toutiao.com/search_content/?'+urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None

def get_images(json):
    if json.get('data'):
        for item in json.get('data'):
            # print('--------------------------------')
            # print(json.get('data'))
            title = item.get('title')
            # images = item.get('image_detail')
            images = item.get('image_list')
            for image in images:
                yield{
                    'image':"https:"+image.get('url'),
                    'title':title
                }

import os
from hashlib import md5

def save_image(item):

    dir_ = 'D:/WorkSpace/PyCharm/intelligent/com/datas/crawler_data/toutiao/'
    str1 = item.get('title')
    str2 = str1.split("：")
    str3 = str2[0].split("，")
    str4 = str3[0].split(" ")
    str5 = str4[0].split("！")
    s =str5[0]
    # dir_str =dir_ + str5[0]
    # ds = str(s)
    if not os.path.exists(s):
        os.mkdir(s)
    try:
        response = requests.get(item.get('image'))
        if response.status_code == 200:
            # dir_ = 'D:/WorkSpace/PyCharm/intelligent/com/datas/crawler_data/toutiao/'
            file_path = '{0}/{1}.{2}'.format(s,md5(response.content).hexdigest(),'jpg')
            if not os.path.exists(file_path):
                with open(file_path,'wb') as f:
                    f.write(response.content)
            else:
                print('Already Downloaded',file_path)
    except requests.ConnectionError:
        print('Failed to Save Image')

from multiprocessing.pool import Pool

def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        save_image(item)

GROUP_START = 1
GROUP_END = 20

if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START,GROUP_END+1)])
    pool.map(main,groups)
    pool.close()
    pool.join()
