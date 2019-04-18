#!/usr/bin/env python
# encoding: utf-8


from flask import Flask
import config


app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
def index():
    print('hello')
    return 'hello world!'

@app.route('/list/')
def my_list():

    return "list"


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=8000)
    app.run()
