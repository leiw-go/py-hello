#!/usr/bin/python3

#运行这个程序会报错，如果想运行请把报错信息中的ip地址发给我

import http.client
import hashlib
import urllib
import random
import json
import os

appid = '20201214000646738' 
secretKey = 'oLmXEsUYZ6X4oR13oSgW'  

httpClient = None
myurl = '/api/trans/vip/translate'

fo = open("source.txt", "r+",encoding = 'utf-8')

fromLang = 'auto'   #原文语种
toLang = 'zh'   #译文语种
salt = random.randint(32768, 65536)
q= fo.read()
sign = appid + q + str(salt) + secretKey
sign = hashlib.md5(sign.encode()).hexdigest()
myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
salt) + '&sign=' + sign

try:
    httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
    httpClient.request('GET', myurl)

    # response是HTTPResponse对象
    response = httpClient.getresponse()
    result_all = response.read().decode("utf-8")
    result = json.loads(result_all)

    # print (result['trans_result'][0]['dst'])

    str = result["trans_result"][0]['dst']
    f = open("translated.txt", "a")
    f.write('\n'+str)
    f.flush()
    f.close

    print("Successful Translating!")

except Exception:
    print (result)
finally:
    if httpClient:
        httpClient.close()
os.system("python qqmail.py")