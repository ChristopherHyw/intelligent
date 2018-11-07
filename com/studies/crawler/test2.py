import requests
import re
import json
def get_one_page(url):
    headers = {
        'User-Agent':'MoZilla/5.0 (Macintosh;Intel Mac OS X 10_13_2) AppleWebKit/537.36(KHTML,like Gecko) Chrome/65.0.3325.162 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    if response.status_code ==200:
        return response.text
    return None

def parse_one_page(html):
    pattern = re.compile('<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',re.S)
    items = re.findall(pattern,html)
    for item in items:
        yield {
            'index':item[0],
            # 'image':item[1],
            'title':item[2].strip(),
            # 'actor':item[3].strip()[3:] if len(item[3]) > 3 else '',
            # 'time':item[4].strip()[5:] if len(item[4]) > 5 else '',
            # 'score':item[5].strip() + item[6].strip(),
        }

def write_to_file(content):
    with open('D:/WorkSpace/PyCharm/intelligent/com/datas/crawler_data/result.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')

def main(offset):
    url = 'http://maoyan.com/board/4?offset='+str(offset)
    html = get_one_page(url)
    results = parse_one_page(html)
    for item in results:
        write_to_file(item)

if __name__ == '__main__':
    for i in range(10):
        main(offset=i*10)
