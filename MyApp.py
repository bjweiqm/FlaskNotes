#!/usr/bin/env python
# encoding: utf-8


from flask import Flask, render_template, url_for
from common.lottery.lottery_result import run, lottery_number


app = Flask(__name__)
app.config.update({
    'DEBUG': True,
    'TEMPLATE_AUTO_RELOAD': True,
})


@app.route('/')
def index():
    respons = lottery_number()
    ssq, dlt = run()
    respons['ssq_prize'] = prize[-1]
    respons['dlt_prize'] = prize[0]
    print('222222222')
    print(ssq)
    print('333333333')
    print(dlt)
    return render_template('MyIndex.html', **respons)

@app.route('/add/')
def add_number():

    return render_template('add_nuber.html')


if __name__ == '__main__':
    app.run()
