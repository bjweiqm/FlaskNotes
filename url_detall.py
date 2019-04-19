#!/usr/bin/env python
# encoding: utf-8


from flask import Flask, render_template, request
import config


app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
def index():
    print('hello')
    return 'hello world!'

@app.route('/list/', methods=["POST"])
def my_list():

    return "list"


@app.route('/login/', methods=["POST", 'GET'])
def login():
    if request.method == "GET":
        return render_template('url_detall_index.html')
    else:
        return 'success'


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=8000)
    app.run()
