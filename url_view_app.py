#!/usr/bin/env python
# encoding: utf-8


from flask import Flask,request
import config


app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
def hell_world():

    return 'hello world!'

@app.route('/list/')
def article_list():
    
    return 'article_list'

@app.route('/<int:id>/')
def detail_id(id):

    return 'detail_id'

@app.route('/<float:float>/')
def detail_float(float):

    return 'detail float'

# @app.route('/<path:path>/')
# def detail_path(path):

#     return 'path{}'.format(path)


import uuid
print(uuid.uuid4())

@app.route('/uuid/<uuid:uuid>/')
def detail_uuid(uuid):
    
    return '用户个人中心={}'.format(uuid)

@app.route('/<any(blog, user):url_path>/<id>')
def detail(url_path, id):
    if url_path == 'blog':
        return 'blog detail'
    else:
        return 'user detail'

# 通过?`问号`传递参数
@app.route('/d/')
def d():
    wd = request.args.get('wd')
    id = request.args.get('id') # 接受多个参数，参数使用&符号分割。
    return "您传递的参数是{}id{}".format(wd, id)



if __name__ == '__main__':
    app.run()
