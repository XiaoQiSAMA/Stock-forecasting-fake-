'''金开......信息'''
import requests
from lxml import etree
def get_page_info(code):  # 获取页面信息
    base_url='https://gupiao.baidu.com/stock/'
    url=base_url+code+'.html'
    headers = {
        'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 75.0.3770.142Safari / 537.36',
        'Referer': 'https:// gupiao.baidu.com / stock / sh000001.html',
        'Host': 'gupiao.baidu.com',
        'Cookies': 'BAIDUID=D7F1C4037D110A61867B822F83B8CE3C:FG=1; BIDUPSID=D7F1C4037D110A61867B822F83B8CE3C; PSTM=1552279033; BDUSS=VZPYUhVOGhjWWw2bjYyUTIydGxqTU5BOEkwZ3dNamZNbXRVMzZFUmdKZmR-N05jQVFBQUFBJCQAAAAAAAAAAAEAAAAd92FiVGhlU2t5bGllcgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAN1yjFzdcoxcO; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_PS_PSSID=1424_21088_29523_29519_28519_29099_28831_29221_29072; delPer=0; PSINO=5; Hm_lvt_35d1e71f4c913c126b8703586f1d2307=1563537057,1563539471,1563540929,1563540940; Hm_lpvt_35d1e71f4c913c126b8703586f1d2307=1563540972'
    }
    resp = requests.get(url,headers)
    if resp.status_code == 200:
        return resp.content.decode('utf-8')
    else:
        print("Error")
    return url

def parse_page_info(stock_code):
    text = get_page_info(stock_code)
    html = etree.HTML(text)
    result1=html.xpath('//div[@class="bets-content"]/div/dl/dt/text()')
    result2=html.xpath('//div[@class="bets-content"]/div/dl/dd/text()')
    for i in range(0,len(result1)):
       result1[i]=result1[i].strip()
       result2[i]=result2[i].strip()
    try:
        result2.pop(6)
        result1.pop(6)
        result2.pop(17)
        result1.pop(17)
    except IndexError:
        pass

    return result1,result2

def transform(result1,result2):

    str=''
    for i in range(0,int(len(result1)/2)):
        str+='{name:<{len}}\t'.format(name=result1[i],len=8-len(result1[i].encode('GBK'))+len(result1[i]))

    str+="\n"
    for i in range(0, int(len(result2) / 2)):
        str+='{name:<{len}}\t'.format(name=result2[i],len=8-len(result2[i].encode('GBK'))+len(result2[i]))

    str+='\n'
    for i in range(int(len(result1)/2),int(len(result1))):
        str += '{name:<{len}}\t'.format(name=result1[i], len=8 - len(result1[i].encode('GBK')) + len(result1[i]))

    str+='\n'
    for i in range(int(len(result1) / 2), int(len(result1))):
        str+='{name:<{len}}\t'.format(name=result2[i],len=8-len(result2[i].encode('GBK'))+len(result2[i]))

    return str

