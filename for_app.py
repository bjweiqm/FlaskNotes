#!/usr/bin/env python
# encoding: utf-8


from flask import Flask, render_template


app = Flask(__name__)
app.debug = True
app.templates_auto_reload = True


@app.route('/')
def index():
    context = {
        'users': ['user1', 'user2', 'user3'],
        # 'users': [],
        'info': {
            'name': 'zhangsan',
            'age': 20,
            'country': 'china'
        },
        'books': [{
            'name': '三国演义',
            'author': '罗贯中',
            'price': 110,
        },
        {
            'name': '水浒传',
            'author': '施耐庵',
            'price': 100,
        },
        {
            'name': '西游记',
            'author': '吴承恩',
            'price': 130,
        },{
            'name': '红楼梦',
            'author': '曹雪芹',
            'price': 119,
        }]
    }

    return render_template('for_app.html', **context)


if __name__ == '__main__':
    app.run()
