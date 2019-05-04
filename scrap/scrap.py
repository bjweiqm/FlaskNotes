#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   scrap.py
@Time    :   2019/05/04 14:13:35
@Author  :   WM 
@Version :   1.0
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

import random, requests, re, sys
from config import user_agent


# 浏览器请求头User-Agent
headers = {
    'User-Agent': random.choice(user_agent)
}
# url = 'http://www.caca043.com/videos/60657/742baa1fe8c3238014e6bc5bc3885464/'


# 写入文件
def write_data(data):

    with open('data.html', 'wb') as files:
        files.write(bytes(data, 'utf-8'))

def re_respons():
    # pre = re.compile(r"rnd: '\d{10}',\s?video_url: '^http.*?\d$',")
    with open('data.html', 'r', encoding='utf-8') as files:
        strings = files.read()

    print(strings)
    print('-' * 30)
    
    rnd = re.findall(r"rnd: '(\d{8,13})'", strings)
    link = re.findall(r"video_url: '(http.*?)'", strings)
    print(rnd[0])
    print(link[0])
    print('{}&rnd={}'.format(link[0], rnd[0]))


def jiexi_url(data):
    rnd = re.findall(r"rnd: '(\d{8,13})'", data)
    url = re.findall(r"video_url: '(http.*?)'", data)
    return '{}&rnd={}'.format(url[0], rnd[0])



def run(url):
    req = requests.get(url=url, headers=headers)

    if req.status_code == 200:
        download_url = jiexi_url(req.text)
        print(download_url)
        # write_data(req.text)
        # print(req.text)
    else:
        print('-' * 30)
        print(req.text)




if __name__=='__main__':
    url = 'http://www.caca043.com/videos/60657/742baa1fe8c3238014e6bc5bc3885464/'
    # re_respons()
    # try:
    #     args = sys.argv[1]
    #     print(args)
    # except IndexError as identifier:
    #     pass
    run(url)
#    print(headers)
