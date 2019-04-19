#!/usr/bin/env python
# encoding: utf-8


from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello_world():

    return render_template()


if __name__ == '__main__':
    app.run()
