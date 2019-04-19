#!/usr/bin/env python
# encoding: utf-8
'''
flask = werkzeng + sqlalchemy + jinja2
'''

from flask import Flask, Response


app = Flask(__name__)
app.debug = True


@app.route('/')
def index():

    return 'holle world !!'

@app.route('/list1/')
def list1():

    return {'zhangsan': 'lisi'}


if __name__ == '__main__':
    app.run()
