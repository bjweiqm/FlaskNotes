# 文件上传及访问

1. 在模板中， form中，需要指定 enctype="multipart/form-data" 才能上传文件。
2. 在后台如果想要获取上传的文件，那么应该使用 request.files.get('filename') 来过去。
3. 保存文件之前，先要使用 werkzeng.utils.secure_filename 来对上传上来的文件名进行一个过滤。这样才能保证不会有安全漏洞。
4. 获取到上传上来的文件后，使用 avatar.save(路径) 来保存文件。
5. 从服务器上读取文件，应该定义一个URL来获取指定的文件，并且在这个URL视图函数中使用 send_from_directory(文件的目录，文件名) 来获取。

实例代码：

```python
from flask import Flask,render_template, request, send_from_directory
from werkzeug.utils import secure_filename
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

        desc = request.form.get('desc')
        avatar = request.files.get('avatar')
        # 过滤用户名是否安全
        filename = secure_filename(avatar.filename)
        avatar.save(os.path.join(UPLOAD_PATH, filename))
        print(desc)
        return '文件上传成功'


@app.route('/images/<filename>/')
def get_image(filename):

    return send_from_directory(UPLOAD_PATH, filename)


if __name__ == '__main__':
    app.run()

```

## 上传文件上传表单

1. 定义表单的时候，对文件字段，需要采用 FileField 这个类型
2. 验证器应该从 flask_wtf.file 中导入 flask_wtf.file.FileRequired 是用来验证文件上传是否为空，flask_wtf.file.FileAllowed 是用来验证文件上传的文件后缀名
3. 在试图文件中，使用 werkzeug.datastructures.CombinedMultiDict 来把 request.form 与 request.files 进行合并，再传给表单来验证。

实例代码如下

```python
from werkzeug.datastructures import CombinedMultiDict
form  = UploadForm(CombinedMultiDict([request.form, request.files]))
```
