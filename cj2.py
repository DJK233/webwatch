import urllib.request
from bs4 import BeautifulSoup
import requests
import time
url_list=['http://www.niaot.ac.cn/xwzx/tzgg/']
tmp = {'history':None}
api = "https://sctapi.ftqq.com/SCT7313TVj2zEdoINtSaZJZ8e9uRsWFs.send"
title = "天光所有新通知啦"
#定义一个名为get_webInfo的函数，传入参数url
def get_webInfo(url):
    head = {}
    head['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0' 
    req = urllib.request.Request(url,headers=head)
    rsp = urllib.request.urlopen(req)
    html = rsp.read().decode('utf8','ignore')
    html = BeautifulSoup(html,'html.parser')
    for link in html.find_all('a',limit=86):
        info_link = link.get('href')
        info_text = link.get_text(strip=True)
    #函数执行完后，return(输出)执行的结果
    url1='http://www.niaot.ac.cn/xwzx/tzgg/'
    return info_text+'\n'+url1+info_link+'\n'
    
def parseWeb(url_list):
    #初始化result为一个列表
    result = [1]
    for url in url_list:
        #每循环一次，就调用get_webInfo，传入参数url，解析出结果，存入变量webInfo
        webInfo = get_webInfo(url)
        print(webInfo)
        hisroty=webInfo
        #每循环一次，就将解析结果放入result列表中
        result.append(webInfo)
   # 函数执行结束后，return(输出) result
    return result


def check():
    #判断字典内的元素history不为空
    if (tmp['history']):
        #把临时值给tmp字典内的history元素 用于循环比较
        hisroty = tmp['history']
        now = parseWeb(url_list)
           #if (len(history) == len(now)):
            #定义一个空的变量 result
        result=''
                #使用zip函数，对history和now函数按顺序进行对比
        
        if hisroty == now:
                        print('未发现更新！')
                        #result=now
                        data = {
                                "text":title,
                                "desp":result
                                }
                        #req = requests.post(api,data = data)
            
        else:
                        print('发现更新')
                        #等价于result=result+b 发现更新就在变量result内添加内容，不会覆盖
                        result=now
                        tmp['history'] = now
                        data = {
                                "text":title,
                                "desp":result
                                }
                        req = requests.post(api,data = data)
            
                        #注意空格，上面for循环执行后才会执行下面的if判断
                            #为防止误判，两次获取内容都为空也满足len(history)==len(now),对result进行非空判断
        if result != '':
        #输出结果
                    print('更新内容如下:'+str(result))
           # else:
               # print('数据错误！')
                #比较完成后把值覆盖传递
        tmp['history'] = now
    else:
        #如果tmp里的history元素为空则判定第一次运行
        tmp['history'] = parseWeb(url_list)



while True:
    check()
    print('\n休息30秒继续运行！')
    time.sleep(360)
    print('继续工作...')
