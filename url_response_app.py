#!/usr/bin/env python
# encoding: utf-8


from flask import Flask


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
