#! python3.7
import urllib.request
import re


def getHtml():
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}

    url = "https://gupiao.baidu.com/"

    req = urllib.request.Request(url,headers = headers)

    res = urllib.request.urlopen(req)

    if res.getcode() != 200:
        print('error')
        exit(1)
    html = res.read().decode('utf-8')
    return html

def getTarget(html):
    
    target = re.compile('<a href="/stock/(.*?).html"\n\
                            title="(.*?)" target="_blank"\n\
                            data-spm="(.*?)">\n\
                            <div>(.*?)</div>\n\
                            <div class="code">(.*?)</div>\n\
                        </a>')
                                
    kind_target = re.compile('<a class="concept-header column1" href="/concept/(.*?).html" target="_blank" data-spm="(.*?)">\n\
                <h2 class="text-ellipsis" title="(.*?)">\n\
                    (.*?)</h2>\n\
                <h3>热搜指数: <span>(.*?)</span></h3>\n\
                <p(.*?)</p>\n\
                <p>(.*?)</p>\n\
            </a>')
    j = 0
    k = 0

    res = list()



    for i in target.findall(html):
        if j % 3 == 0:
            item ={}
            kind_list = list(kind_target.findall(html))
            kind = list(kind_list[k])
            k+=1
            res.append({'title':kind[2],'hot':kind[4],'data':item})
        j+=1
        target_list = list(i)
        item[target_list[1]] = target_list[0]
    return res

if __name__ == '__main__':
    print(getTarget(getHtml()))