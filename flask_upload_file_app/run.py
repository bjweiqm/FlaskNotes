#!/usr/bin/env python
# encoding: utf-8


from flask import Flask,render_template, request, send_from_directory
from forms import UploadForm
from werkzeug.utils import secure_filename
from werkzeug.datastructures import CombinedMultiDict
import os


app = Flask(__name__)

UPLOAD_PATH = os.path.join(os.path.dirname(__file__), 'images')


@app.route('/')
def index():

    return 'hello Word ！'


@app.route('/upload/', methods=["GET", "POST"])
def upload():
    if request.method == "GET":
        return render_template('upload.html')
    else:
        # CombinedMultiDict 整合 描述 与 文件信息，在UploadForm 中对比过滤
        form  = UploadForm(CombinedMultiDict([request.form, request.files]))
        if form.validate():
            # 获取描述信息
            # desc = request.form.get('desc')
            # 图片文件信息
            # avatar = request.files.get('avatar')
            # 过滤用户名是否安全
            # 另一种获取表单的方式
            desc = form.desc.data
            avatar = form.avatar.data
            filename = secure_filename(avatar.filename)
            avatar.save(os.path.join(UPLOAD_PATH, filename))
            print(desc)
            return '文件上传成功'
        else:
            print(form.errors)
            return 'fail'


@app.route('/images/<filename>/')
def get_image(filename):

    return send_from_directory(UPLOAD_PATH, filename)


if __name__ == '__main__':
    app.run()
