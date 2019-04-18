#!/usr/bin/env python
# encoding: utf-8

'''自定义URL转换器
'''

from flask import Flask, url_for
from werkzeug.routing import BaseConverter
import config


app = Flask(__name__)
app.config.from_object(config)


class TelephoneConverter(BaseConverter):
    # 一个URL中含有手机号码的变量，必须先定这个变量格式满足手机号码的格式
    regex = r'1[85734]\d{9}'
# 把写好的参数类型注册到converters中


class ListConverter(BaseConverter):
    # 用户在访问/posts/a+b/(集合两个板块的内容)
    # to_python 方法
    # to_url 方法

    def to_python(self, value):
        print(value)
        return value.split('+')

    def to_url(self, value):
        print(value)
        
        return 'hello=={}'.format('+'.join(value))

app.url_map.converters['tel'] = TelephoneConverter
app.url_map.converters['list'] = ListConverter


@app.route('/')
def index():
    print(url_for('posts', boards=['a', 'b']))
    return 'hello world!'

@app.route('/user/<int:user_id>/')
def user_profile(user_id):

    return "您输入的user_id为：{}".format(user_id)


@app.route('/telephone/<tel:my_tel>/')
def my_tel(my_tel):

    return "输入的手机号为：{}".format(my_tel)

@app.route('/posts/<list:boards>/')
def posts(boards):
    print(boards)
    return "提交的板块是：{}".format(boards)


if __name__ == '__main__':
    app.run()

