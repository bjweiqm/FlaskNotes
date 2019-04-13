#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   app.py
@Time    :   2019/04/13 08:46:32
@Author  :   WM 
@Version :   1.0
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

from flask import Flask, render_template


app = Flask(__name__)
app.config.update({
    "DEBUG": True,
    "TEMPLATES_AUTO_RELOAD": True
})

@app.route('/')
def index():
    deta.json = {
        'html': '<h1>首页</h1>'
    }  
    
    return render_template()


if __name__=='__main__':
   print('ceshi')