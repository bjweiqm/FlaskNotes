#!/usr/bin/env python
# encoding: utf-8


from flask import Flask, render_template


app = Flask(__name__)
app.debug = True


@app.route('/')
def index():

    return render_template('template_url_for_index.html')


@app.route('/login/')
def login():

    return render_template('template_url_for_login.html')


if __name__ == '__main__':
    app.run()
