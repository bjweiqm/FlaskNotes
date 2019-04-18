#!/usr/bin/env python
# encoding: utf-8


from flask import Flask, url_for, request
import config


app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
def index():

    return url_for('login', next='/')


@app.route('/list/<page>/')
def my_list(page):

    return 'my_list'

@app.route('/login/')
def login():

    return 'login'

if __name__ == '__main__':
    app.run()
