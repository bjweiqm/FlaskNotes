#!/usr/bin/env python
# encoding: utf-8


from flask import Flask
import config


app = Flask(__name__)
# app.config.from_object(config)    # 加载配置文件的方式
app.config.from_pyfile('config.py'， silent=False) # 使用文件的方式加载配置文件 silent=False 表示：忽略路径错误。


@app.route('/')
def index():
    return 'hello world!'


if __name__ == '__main__':
    app.run()
