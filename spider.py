import requests
import json
from requests.exceptions import MissingSchema

session = requests.Session()

class Spider:

    # 爬虫模块
    class Search:
        # 搜索模块
        def __init__(cls, key):
            cls.key = key
            cls._search_url = 'https://gupiao.baidu.com/api/search/stockquery?from=pc&os_ver=1&cuid=xxx&vv=3.2&format=json&asset=0%2C4%2C14&timestamp=1563542035454&query_content='

        # 检索模块
        headers = {
            'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 75.0.3770.142Safari / 537.36',
            'Referer': 'https:// gupiao.baidu.com / stock / sh000001.html',
            'Host': 'gupiao.baidu.com',
            'Cookies': 'BAIDUID=D7F1C4037D110A61867B822F83B8CE3C:FG=1; BIDUPSID=D7F1C4037D110A61867B822F83B8CE3C; PSTM=1552279033; BDUSS=VZPYUhVOGhjWWw2bjYyUTIydGxqTU5BOEkwZ3dNamZNbXRVMzZFUmdKZmR-N05jQVFBQUFBJCQAAAAAAAAAAAEAAAAd92FiVGhlU2t5bGllcgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAN1yjFzdcoxcO; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1424_21088_29523_29519_28519_29099_28831_29221_29072; delPer=0; PSINO=5; Hm_lvt_35d1e71f4c913c126b8703586f1d2307=1563537057,1563539471,1563540929,1563540940; Hm_lpvt_35d1e71f4c913c126b8703586f1d2307=1563540972'
        }


        def make_urls(self):  # 构造股票urls
            return self._search_url + str(self.key)

        def get_page_info(self, url):  # 获取页面信息
            resp = session.post(url, self.headers)
            if resp.status_code == 200:

                return resp.text
            else:
                print("Error")


        def return_info(self):  # 数据处理
            url = self.make_urls()
            page_info = self.get_page_info(url)

            page_info = json.loads(page_info)

            # try:
            try:
                stock_data = page_info['data']['stock_data'][0]
                return {                                            #构造股票信息字典返回
                    'stock_name': stock_data['f_symbolName'],
                    'stock_code': stock_data['f_code'],
                    'stock_fullname': stock_data['f_fullName']
                }
            except IndexError:
                pass

    class Process:

        def __init__(self, dict):

            self.dict = dict


        def make_url(self, dict): # 构造url

            try:
                url = f'https://gupiao.baidu.com/api/stocks/stocktimeline?from=pc&os_ver=1&cuid=xxx&vv=100&format=json&stock_code={dict["stock_code"]}&timestamp=1563547803652'
                return url
            except TypeError:
                pass

        def make_stock_page(self, url):  # 处理当前股票网页的数据(巨额交易)  只读json格式网页
            resp = requests.get(url)
            resp = json.loads(resp.text)
            return resp

        def search_page(self):

            url = self.make_url(self.dict)
            try:
                resp = requests.get(url)
                resp = json.loads(resp.text)
                return resp                         #搜索返回的股票数据
            except MissingSchema:
                pass

