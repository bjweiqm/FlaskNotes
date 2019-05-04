#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   scra.py
@Time    :   2019/05/04 15:38:45
@Author  :   WM 
@Version :   1.0
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''


import random, requests, re, sys
from config import user_agent


def re_deta(data):
    '''解析data数据中的数据，分析出下载地址
    '''
    rnd = re.findall(r"rnd: '(\d{8,13})'", data)
    url = re.findall(r"video_url: '(http.*?)'", data)
    return '{}&rnd={}'.format(url[0], rnd[0])


def get_url_data(url):
    respon = requests.get(url, headers={'User-Agent': random.choice(user_agent)})
    if respon.status_code == 200:
        download = re_deta(respon.text)
        print(download)
        return download


if __name__=='__main__':
    url = 'http://www.caca043.com/videos/46991/91-104/'
    get_url_data(url)