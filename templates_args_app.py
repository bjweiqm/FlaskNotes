#!/usr/bin/env python
# encoding: utf-8


from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def hello_world():
    context = {
        'name': 'zhiliao',
        'age': 18,
        'country': 'china'
    }
    return render_template('templates_args_index.html', name='zhiliao')


if __name__ == '__main__':
    app.run()
