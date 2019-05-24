#!/usr/bin/env python
# encoding: utf-8


from flask import Flask,render_template, request
import config


app = Flask(__name__)
app.config.from_object(config)

movies = [
    {
        'id': 38723,
        'title': '黄飞鸿',
        'rating': 5.6,
        'thumbnail': 'https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2494515769,1618681702&fm=26&gp=0.jpg'
    },
    {
        'id': 38723,
        'title': '黄飞鸿',
        'rating': 5.6,
        'thumbnail': 'https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2494515769,1618681702&fm=26&gp=0.jpg'
    },
    {
        'id': 38723,
        'title': '黄飞鸿',
        'rating': 5.6,
        'thumbnail': 'https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2494515769,1618681702&fm=26&gp=0.jpg'
    },
    {
        'id': 38723,
        'title': '黄飞鸿',
        'rating': 5.6,
        'thumbnail': 'https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2494515769,1618681702&fm=26&gp=0.jpg'
    },
    {
        'id': 38723,
        'title': '黄飞鸿',
        'rating': 5.6,
        'thumbnail': 'https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2494515769,1618681702&fm=26&gp=0.jpg'
    },
    
]
tvs = [
    {
        'id': 38723,
        'title': '黄飞鸿',
        'rating': 5.6,
        'thumbnail': 'https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2494515769,1618681702&fm=26&gp=0.jpg'
    },
    {
        'id': 38723,
        'title': '黄飞鸿',
        'rating': 5.6,
        'thumbnail': 'https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2494515769,1618681702&fm=26&gp=0.jpg'
    },
    {
        'id': 38723,
        'title': '黄飞鸿',
        'rating': 5.6,
        'thumbnail': 'https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2494515769,1618681702&fm=26&gp=0.jpg'
    },
    {
        'id': 38723,
        'title': '黄飞鸿',
        'rating': 5.6,
        'thumbnail': 'https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=2494515769,1618681702&fm=26&gp=0.jpg'
    },
    {
        'id': 38723,
        'title': '黄飞鸿',
        'rating': 5.6,
        'thumbnail': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1559301166&di=c734183bca69c92b49a233b8c9ad0610&imgtype=jpg&er=1&src=http%3A%2F%2Fpic18.nipic.com%2F20120130%2F7286812_154518084332_2.jpg'
    },
]


@app.route('/')
def index():
    context = {
        'moives': movies,
        'tvs': tvs
    }

    return render_template('douban/index.html', **context)

@app.route('/item_list/')
def item_list():
    category = request.args.get('category')
    if category == 1:
        items = movies
    else:
        items = tvs
    return render_template('douban/list.html', items = items)    


if __name__ == '__main__':
    app.run()
