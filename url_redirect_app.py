#!/usr/bin/env python
# encoding: utf-8


from flask import Flask,redirect, request, url_for


app = Flask(__name__)
app.debug = True

@app.route('/')
def index():

    return "hello index"

@app.route('/login/')
def login():

    return 'login Page'

@app.route('/profile/')
def profile():

    if request.args.get('name'):
        return '欢迎来到个人中心'
    else:
        # return redirect("/login/")
        return redirect(url_for('login'), code=302)

if __name__ == '__main__':
    app.run()
