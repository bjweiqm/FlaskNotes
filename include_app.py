#!/usr/bin/env python
# encoding: utf-8


from flask import Flask, render_template


app = Flask(__name__)
app.debug = True
app.templates_auto_reload = True


@app.route('/')
def index():
    
    return render_template('include_app.html')


if __name__ == '__main__':
    app.run()
