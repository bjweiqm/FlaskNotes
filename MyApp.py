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
    if isinstance(respons, dict):
        ssq = respons.get('ssq_red')
        dlt = respons.get('dlt_blue')
        print(type(dlt))
        print(ssq[0])
        print('---'*40)
        print('{}\n{}'.format(ssq, dlt))

    # print(respons)
    return render_template('MyIndex.html', **respons)


if __name__ == '__main__':
    app.run()
