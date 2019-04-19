#!/usr/bin/env python
# encoding: utf-8
'''
flask = werkzeng + sqlalchemy + jinja2
'''

from flask import Flask, Response, jsonify
# from werkzeug.wrappers import Response


app = Flask(__name__)
app.debug = True


# 将视图函数中返回字典，转换成json对象然后返回
# restful-api


class JsonReponse(Response):
    @classmethod
    def force_type(cls, response, environ=None):
        '''
        这个方法只有视图函数返回非字符串、元组、Response对象，才会调用。
        '''
        # print(response)
        # print(type(response))
        if isinstance(response, dict):
            # jsonify 除了将字典转换为json对象，还将该对象包装成了一个Response对象。
            response = jsonify(response)
        return super(JsonReponse, cls).force_type(response, environ)
        # return Response('hello')


app.response_class = JsonReponse

@app.route('/')
def index():

    # Response("hello world", status=200, mimetype="text/html")
    return 'holle world !!'

@app.route('/list1/')
def list1():

    return 'list1', 200, {'X-NAME': 'zhiliao'}


@app.route('/list2/')
def list2():

    return {'username': 'zhiliao', 'age': 18}

@app.route('/list3/')
def list3():
    # 这种方法可以设置cookie
    res = Response('hello')
    res.set_cookie('country', 'china')
    return res
    # return Response('hello')


if __name__ == '__main__':
    app.run()
