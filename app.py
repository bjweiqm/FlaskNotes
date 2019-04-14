#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   app.py
@Time    :   2019/04/13 08:46:32
@Author  :   WM 
@Version :   1.0
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''
# 从flask这个包中导入Flask类
# Flask这个类是项目的核心，以后很多操作都是基于这个类的对象
# 注册url，注册蓝图等都是基于这个类的对象
from flask import Flask, render_template

#创建一个Flask对象，传递一个__name__参数进去
#__name__参数的作用：
#1. 可以规定模板和静态文件的查找路径
#2. 以后一些Flask插件，比如Flask-migrate、Flask-SQLAlchemy如果报错了，那么flask
#可以通过这个参数找到具体的报错位置
app = Flask(__name__)

app.config.update({
    # 开启debug模式，
    "DEBUG": True,
    # 开启自动加载模式，修改静态资源后，无需重新启动服务器。
    "TEMPLATES_AUTO_RELOAD": True
})

# @app.route('/') 是一个装饰器
# @app.route('/') 就是将url中的/映射到index这个视图函数上面
# 以后你访问我这个网站的/目录的时候，会执行index这个函数，然后将这个函数的返回值返回给浏览器
@app.route('/')
def index(): 
    
    return render_template('index.html')

@app.route('/list/')
def my_list():
    return 'My List!'


# 如果这个文件作为主文件运行，那么就执行app.run()方法
# 也就是启动这个网站
if __name__=='__main__':
   app.run()