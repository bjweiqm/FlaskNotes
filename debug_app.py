#!/usr/bin/env python
# encoding: utf-8

import config
from flask import Flask

app = Flask(__name__)
# app.config.update(DEBUG=True)  # 开启debug模式的另一种方法，修改字典模式
app.config.from_object(config)   # 开启debug模式的另一中方法，读取文件形式

@app.route('/')
def index():
    
    a = 1
    b = 0
    c = a / b
    return 'hello world!!'



if __name__ == '__main__':
    # debug 开启
    app.run()