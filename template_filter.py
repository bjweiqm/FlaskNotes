#!/usr/bin/env python
# encoding: utf-8


from flask import Flask, render_template
from datetime import datetime


app = Flask(__name__)
app.debug = True
app.templates_auto_reload = True


@app.route('/')
def index():
    context = {
        'create_time': datetime(2019, 5, 16, 17, 30, 0, 0)
    }
    return render_template('filter.html', **context)

@app.template_filter('handle_time')
def handle_time(time):
    '''
    time距离现在的时间间隔
    1. 如果间隔小于1分钟，那么就显示刚刚
    2. 如果是1小时内，那么就显示xx分钟
    3. 如果是24小时内，那么就显示xx小时
    4. 如果是30天内，那么就显示xx天
    5. 否则就显示具体的时间
    '''
    if isinstance(time, datetime):
        now = datetime.now()
        timestamp = (now - time).total_seconds()
        if timestamp < 60:
            return "刚刚"
        elif timestamp >= 60 and timestamp < 60 * 60:
            minutes = timestamp / 60
            return '{}分钟前'.format(int(minutes))
        elif timestamp >= 60 * 60 and timestamp < 60 * 60 * 24:
            hours = timestamp / (60 * 60)
            return '{}小时前'.format(int(hours))
        elif timestamp >= 60 * 60 * 24 and timestamp < 60 * 60 * 24 * 30:
            day = timestamp / (60 * 60 * 24)
            return '{}天前'.format(int(day))
        else:
            return time.strftime('%Y/%m/%d %H:%M')
    else:
        return time
    return 


if __name__ == '__main__':
    app.run()
