#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   LotteryApp.py
@Time    :   2019/02/16 12:38:52
@Author  :   WM 
@Version :   1.0
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

import requests
from bs4 import BeautifulSoup


dlt_blue = set([5, 7])
dlt_red = set([4, 5, 8, 10, 28])
ssq_blue = set([12])
ssq_red = set([4, 5, 7, 8, 12, 28])
dlt_lottery = {
        (5, 2): '\a 恭喜道友，大乐透喜提一等奖！！',
        (5, 1): '\a 恭喜道友，大乐透喜提二等奖！！',
        (5, 0): '\a 恭喜道友，大乐透喜提三等奖！！',
        (4, 2): '\a 恭喜道友，大乐透喜提三等奖！！',
        (4, 1): '\a 恭喜道友，大乐透喜提四等奖！！',
        (3, 2): '\a 恭喜道友，大乐透喜提四等奖！！',
        (4, 0): '\a 恭喜道友，大乐透喜提五等奖！！',
        (3, 1): '\a 恭喜道友，大乐透喜提五等奖！！',
        (2, 2): '\a 恭喜道友，大乐透喜提五等奖！！',
        (3, 0): '\a 恭喜道友，大乐透喜提六等奖！！',
        (1, 2): '\a 恭喜道友，大乐透喜提六等奖！！',
        (2, 1): '\a 恭喜道友，大乐透喜提六等奖！！',
        (0, 2): '\a 恭喜道友，大乐透喜提六等奖！！',
    }
ssq_lottery = {
        (6, 1): '\a 恭喜道友，喜提双色球一等奖！！',
        (6, 0): '\a 恭喜道友，喜提双色球二等奖！！',
        (5, 1): '\a 恭喜道友，喜提双色球三等奖！！',
        (5, 0): '\a 恭喜道友，喜提双色球四等奖！！',
        (4, 1): '\a 恭喜道友，喜提双色球四等奖！！',
        (4, 0): '\a 恭喜道友，喜提双色球五等奖！！',
        (3, 1): '\a 恭喜道友，喜提双色球五等奖！！',
        (2, 1): '\a 恭喜道友，喜提双色球六等奖！！',
        (1, 1): '\a 恭喜道友，喜提双色球六等奖！！',
        (0, 1): '\a 恭喜道友，喜提双色球六等奖！！',
    }

# print(dlt_blue)
# print(dlt_red)

def html_data(url: str):
    head = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }

    req = requests.get(url, headers=head)
    data = BeautifulSoup(req.text, 'html.parser')   # 把获取到的网页数据抓换成bs4格式，方便解析内容
    lottery_list = data.find_all('div', class_='ball_box01')
    ball_red = set([int(i.string) for i in lottery_list[0].find_all('li', 'ball_red')])
    ball_blue = set([int(i.string) for i in lottery_list[0].find_all('li', 'ball_blue')])
    period = data.find("font", class_='cfont2').string
    print(period)
    print('===='*30)

    return [ball_red, ball_blue, period]


def lottery_dlt(url: str):
    '''大乐透兑奖实现
    {'ssq': [{8, 9, 10, 13, 15, 28}, {9}], 'dlt': [{35, 4, 15, 16, 20}, {3, 12}]}
    '''
    red, blue, period = html_data(url)
    lottery_len = (len(red.intersection(dlt_red)), len(blue.intersection(dlt_blue)))
    if lottery_len in dlt_lottery.keys():

        return dlt_lottery.get(lottery_len)
    else:

        return '哎， 又没中奖！！！'

    
def lottery_ssq(url: str):
    '''双色球兑奖'''
    red, blue, period = html_data(url)
    lottery_len = (len(red.intersection(ssq_red)), len(blue.intersection(ssq_blue)))
    if lottery_len in ssq_lottery.keys():
        print(ssq_lottery.get(lottery_len))
        return ssq_lottery.get(lottery_len)
    else:

        return '哎， 又没中奖！！！'


def lottery_number():
    ssq_url = 'http://kaijiang.500.com/ssq.shtml'
    dlt_url = 'http://kaijiang.500.com/dlt.shtml'
    ssq_red, ssq_blue, ssq_period = html_data(ssq_url)
    dlt_red, dlt_blue, dlt_period = html_data(dlt_url)
    print(ssq_red, ssq_blue, dlt_blue, dlt_red)
    return {
        'ssq_red': list(ssq_red),
        'ssq_blue': list(ssq_blue),
        'dlt_red': list(dlt_red),
        'dlt_blue': list(dlt_blue)
    }

def run():
    ssq_url = 'http://kaijiang.500.com/ssq.shtml'
    dlt_url = 'http://kaijiang.500.com/dlt.shtml'
    return (lottery_dlt(dlt_url), lottery_ssq(ssq_url))



if __name__=='__main__':
    # ssq_url = 'https://caipiao.taobao.com/lottery/drawed/historylist.htm?spm=a2126.12523672.0.0.6cc33348X4Obdm&page=1&type=1'
    # dlt_url = 'https://caipiao.taobao.com/lottery/drawed/historylist.htm?spm=a2126.12523672.0.0.6cc33348X4Obdm&page=1&type=8'
    ssq_url = 'http://kaijiang.500.com/ssq.shtml'
    dlt_url = 'http://kaijiang.500.com/dlt.shtml'
    lottery_dlt(dlt_url)
    lottery_ssq(ssq_url)
