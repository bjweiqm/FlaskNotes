#!/usr/bin/env python
# encoding: utf-8


from flask import Flask,render_template, request, Response


app = Flask(__name__)


@app.route('/')
def index():
    req = Response('studend')
    req.set_cookie('username', 'lisi', max_age=60)

    return req


@app.route('/del/')
def delete():
    req = Response('delect')
    req.delete_cookie('username')
    return req


if __name__ == '__main__':
    app.run(debug=True)

# apolloId:d1543fc0e8274901be01a9d9fcfbf76e
# apolloSecret:162f0903a33a445db6af0461c63c6a3b