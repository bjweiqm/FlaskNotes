#!/usr/bin/env python
# encoding: utf-8


from flask import Flask


app = Flask(__name__)
app.debug = True


@app.route('/')
def index():

    return 'holle world !!'


if __name__ == '__main__':
    app.run()
