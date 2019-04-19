#!/usr/bin/env python
# encoding: utf-8
'''
flask = werkzeng + sqlalchemy + jinja2
'''

from flask import Flask, Response
# from werkzeug.wrappers import Response


app = Flask(__name__)
app.debug = True


# 将视图函数中返回字典，转换成json对象然后返回
# restful-api

@app.route('/')
def index():

    # Response("hello world", status=200, mimetype="text/html")
    return 'holle world !!'

@app.route('/list1/')
def list1():

    return 'list1', 200, {'X-NAME': 'zhiliao'}


if __name__ == '__main__':
    app.run()
