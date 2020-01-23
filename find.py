import requests
from urllib.parse import urlencode
import json

def get_page():
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3029.110 Safari/537.36 SE 2.XMetaSr1.0",
        "referer": "https://www.toutiao.com/search/",
        'x-requested-with': 'XMLHttpRequest'
    }
    params = {
        'from': 'pc',
        'os_ver': '1',
        'cuid': 'xxx',
        'vv': '100',
        'format': 'json',
        'timestamp': '1563585088007'
    }
    base_url = 'https://gupiao.baidu.com/api/rails/hotstocklist?'
    url = base_url + urlencode(params)
    try:
        resp = requests.get(url, headers=headers)
        # print(url)
        if 200 == resp.status_code:
            # print(type(resp.json()))
            # print(resp.json())
            return resp.text
    except requests.ConnectionError:
        return None


def parse_page():
    page_info = get_page()
    # print(type(page_info))
    json_file = json.loads(page_info)
    # print(type(json_file))
    dict = {}
    for item in json_file['data']:
        # # print(item)
        # dict['name'] = item['stockName']
        # # dict.update('name', item['stock_code'])
        # dict['stock_code'] = item['stockCode']
        yield {
            'name': item['stockName'],
            'stock_code': item['stockCode'],
            'exchange': item['exchange']
        }


if __name__ == '__main__':
    for dict in parse_page():
        print(dict['stock_code'])
