#!/usr/bin/env python
# encoding: utf-8


from flask import Flask, render_template, jsonify


app = Flask(__name__)
app.debug = True
app.templates_auto_reload = True


@app.route('/')
def index():
    data = {
        'xAxis': {
            'type': 'category',
            'data': ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        },
        'yAxis': {
            'type': 'value'
        },
        'series': [{
            'data': [820, 932, 901, 934, 1290, 1330, 1320],
            'type': 'line'
        }]
    }
    # print(str(data))
    return render_template('echarts_app.html', data=data)


if __name__ == '__main__':
    app.run()
