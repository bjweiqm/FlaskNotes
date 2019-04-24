[toc]

# 目录

* [第一章：Flask入门](#flask入门)
* [第二章：FlaskURL](#flaskURL)
* [第一章：Flask入门](#第一章：Flask入门)
* [第一章：Flask入门](#第一章：Flask入门)

# FlaskNotes

## 第一章：Flask入门
flask入门

### 1.1 URL详解

URL是Uniform Resource Locator的简写，统一资源定位符

```python
scheme://host:post/path/?query-string=xxx#anchor
```

- scheme: 代表的是访问的协议，一般为HTTP或者HTTPS以及tfp等
- host: 主机名、域名，比如：www.baidu.com
- post: 端口号，当你访问一个网站的时候，浏览器默认使用80端口。
- path: 查找路径，比如：www.jianshu.com/trending/now, 后面的trending/now就是路径
- ？query-string: 查询字符串，比如：www.baidu.com/?wd=python, 后面的wd=python就是查询字符串
- anchor: 锚点，后台一般不用管，前段用来做页面的定位，比如：www.baidu.com/item/xxx/xxx?fr=XXX#7

### 1.2 Flask简介

Flask是一个非常流行的python web框架，出生于2010年，作者是Armin Ronacher, 本来这个项目只是作者愚人节的一个玩笑，后来由于非常受欢迎，进而成为一个正式的项目。

Flask自2010年发布第一版依赖，大受欢迎，深受开发者的喜爱，并且在多个公司已经得到了应用。Flask能够如此流行的原因，可以分为以下几点：

- 微框架，简洁，只做他需要做的，给开发者提供了很大的扩展性。
- Flask和相关的依赖设计的非常优秀，用起来很爽
- 开发效率非常高，比如：SQLAlchemy的ORM操作数据库可以节省大量书写sql的时间。
- 社会活跃度非常高

Flask的灵活度非常之高，他不会帮你做太多的决策，即使已经帮你做出了选择，你也能非常用以更换成你需要的，比如：

- 使用Flask开发数据库时，具体使用SQLAlchemy 还是MogoEngine或者是不用ORM而是直接基于MYSQL-Pyton这样的底层驱动进行开发都是可以的。选择权完全掌握在你自己的手中，区别于Django， Django内置了非常完善和丰富的功能，并且加入如果你想替换成你自己想要的，要么不支持，要么非常麻烦。
- 把默认的Jinjia2模板引擎替换成Mako引擎或者是其他模板引擎是非常容易的。

### 1.3 第一个Flask程序

```python
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
        # 开启debug模式，方便查看错误
        "DEBUG": True,
        # 开启自动加载模式，修改静态资源后，无需重启，自动加载最新静态资源。
        "TEMPLATES_AUTO_RELOAD": True
    })

    # @app.route('/') 是一个装饰器
    # @app.route('/') 就是将url中的/映射到index这个视图函数上面
    # 以后你访问我这个网站的/目录的时候，会执行index这个函数，然后将这个函数的返回值返回给浏览器
    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/my_list/')
    def my_list():
        return 'My list'


    # 如果这个文件作为主文件运行，那么就执行app.run()方法
    # 也就是启动这个网站
    if __name__=='__main__':
    app.run()

```

## 第二章：FlaskURL
flaskURL

### 2.1 Debug模式

#### 2.1.1 为什么需要开启debug模式：

1. 如果开启了debug模式， 那么在代码中如果抛出了异常，在浏览器的页面中可以看到具体的错误信息，以及具体的错误代码位置。方便开发者调试
2. 如果开启了debug模式，那么以后再`Python`代码中修改了任何代码，只要按住 `ctrl + s`， `flask`就会自动的重新加载整个网站，不需要手动点击重新运行。

#### 2.1.2 配置debug模式的四中方式

1. 在 `app.run()`中传递一个参数`debug=True`就可以打开`debug`模式。
2. 给`app.debug=True`,也可以开启`debug`模式
3. 通过配置参数的形式设置debug模式，`app.config.update(DEBUG=True)`
4. 通过配置参数的形式设置debug模式，`app.config.from_object(config)`

#### 2.1.3 pin码

如果想要在网页上调试代码，那么应该输入`pin`码。

### 2.2 config 配置文件

#### 2.2.1 使用`app.config.from_object`的方式加载配置文件

1. 导入`import config`。
2. 使用`app.config.from_object(config)`

#### 2.2.2 使用`app.config.from_pyfile`的方式加载配置文件

这种方式不需要`import`，直接使用`app.config.from_pyfile('config.py')`就可以了。
> 注意：这个地方必须要写文件的全名，后缀不能少。

1. 这种方式，加载配置文件，不局限于使用 `py`文件，普通的`txt`文件同样也适合
2. 这种方式可以传递 `silent=True`， 那么静态文件没有找到的时候不会抛出异常。


### 2.3 URL与试图函数映射

#### 2.3.1 传递参数

传递参数的语法是：`/<参数名>/`，然后在试图函数中，也要定义同名的参数

#### 2.3.2 参数的数据类型

1. 如果没有指定具体的数据类型，那么默认就是使用 `string` 数据类型
2. `int` 数据类型只能传递`int`类型
3. `float` 数据类型只能传递`float`类型
4. `path` 数据类型和`string`有点类似，都是可以接受任意的字符串，但是 `path`可以接受路径，也就是说可以包含斜杠。
5. `uuid` 数据类型只能接受符合 `uuid`的字符串。 `uuid`是一个全宇宙都唯一的字符串。一般可以用来做表的主键
6. `any`数据类型可以在一个URL中指定多个路径，

```python
@app.route('/<any(blog, user):url_path>/<id>')
def detail(url_path, id):
    if url_path == 'blog':
        return 'blog detail'
    else:
        return 'user detail'
```

#### 2.3.3 接收用户传递参数的方式

1. 第一种，就是上面讲的方式（将参数嵌入到路径中）;` 优势：方便搜索引`擎抓取
2. 第二种，就是使用查询的方式，就是通过`?key=value`的形式传递的。
```python
@app.route('/d/')
def d():
    wd = request.args.get('wd')
    return "您传递的参数是{}".format(wd)
```
3. 如果你的页面想要做`SEO`优化，就是被搜索引擎搜索到，那么就推荐使用第一种方式（path的方式），如果不在乎搜索引擎优化，那么就可以使用第二种。（查询字符串的方式）

### 2.4 url_for URL转换器

#### 2.4.1 基本使用

`url_for`第一个参数，应该是试图函数的名字的字符串，后面的参数就是传递给URL。如果传递的参数之前在 URL 中已经定义了，那么这个参数就会被当成 path 的形式给 URL ，如果这个参数之前没有在 URL 中定义，那么奖变成查询字符串的形式放到 URL 中。
```python
    @app.route('/list/<page>/')
    def my_list(page):
        return 'my_list'
    print(url_for('my_list', page=1, count=2))
    # 构建出来的URL：/my_list/1/?count=2
```

#### 2.4.2 为什么需要url_for

1. 将来如果修改了 URL ，但没有修改该 URL 对应的函数名， 就不用到处去替换 URL 了
2. url_for 会自动的处理那些特殊的字符，不需要手动处理。
```python 
    url = url_for('login', next='/')
    # 会自动的将/编码，不需要手动去处理
    # url: /login/?next=%2F
```
> 强烈建议以后再使用URL的时候，使用url_for来反转URL。


#### 2.4.3 自定义URL转换器

##### 2.4.3.1自定义URL转换器的方式
1. 导入`from werkzeug.routing import BaseConverter` 实现一个类，继承自`BaseConverter`
2. 在自定义的类中，重写 `regex`， 也就是这个变量的正则表达式
3. 将自定义的类，映射到`app.url_map.converters`上。例如：
```python
    class TelephoneConverter(BaseConverter):
        # 一个URL中含有手机号码的变量，必须先定这个变量格式满足手机号码的格式
        regex = r'1[85734]\d{9}'
    # 把写好的参数类型注册到converters中
    app.url_map.converters['tel'] = TelephoneConverter
```

##### 2.4.3.2 `to_python`的作用

会将URL中的参数经过解析后传递给视图函数。这个方法的返回值，将会传递到view中作为参数

##### 2.4.3.3 `to_url`的作用

这个方法的返回值，会将在调用url_for函数的时候生成符合要求的URL形式。


#### 2.4.4 必会的小细节知识点

url_detall.py

##### 2.4.4.1 在局域网让其他电脑访问我的网站

如果在一个局域网下的其他电脑访问自己电脑上的Flask网站，那么可以设置 `host='0.0.0.0'`才能访问到。

##### 2.4.4.2 指定端口号

Flask 默认使用5000端口，如果想更换端口，那么可以设置`post=9000`.

##### 2.4.4.3 URL唯一

在定义URL的时候，一定要记得在最后加一个斜杠
1. 如果不加斜杠，那么在浏览器中访问这个URL的时候，如果最后加了斜杠，那么就访问不到，这样用户体验不好
2. 搜索引擎会将不加斜杠的和加斜杠的视为两个不同的URL，而其实加和不加斜杠的都是同一个URL， 那么就会给搜索引擎造成一个误解，加了斜杠，就不会出现没有斜杠的情况。

##### 2.4.4.4 get请求和post请求

在网络请求中有许多请求方式，比如：`get`、`post`、`delete`、`put`请求等，最常用的就是 `get` 和 `]` 请求。
1. `get` 请求：只会在服务器上获取资源，不会更改服务器的状态，这种方式推荐使用get请求。
2. `post`请求： 会给服务器提交一些数据或文件，一般post请求是会对服务器的状态产生影响，那么这种请求推荐使用post请求。
3. 关于传参方式
   1. `get`：把参数请求放到URL中，通过`?xxx=xxx`的形式传输的。
   2. `post`：会把参数放到`Form Data`中。
4. 在`Flask`中，`route`方法，默认将只能使用 get 的方式请求这个URL， 如果想要设置自己的请求方式，那么应该传递一个 `methods` 参数

### 2.5 页面跳转和重定向

重定向分为永久性重定向和暂时性重定向，在页面上体现的操作就是浏览器会从一个页面自动跳转到另外一个页面。比如用户访问了一个需要权限的页面，但是该用户当前并没有登录，因此我们应该给他重定向到登录页面。
- 永久性重定向：HTTP 的状态码是 301， 多用于旧网站被废弃了要转到一个新的网址确保用户访问。
- 暂时性重定向：HTTP 的状态码是 302， 表示页面的暂时性跳转。比如访问一个需要权限的网站，如果当前用户没有登录，应该重定向到登录页面，这种情况下，应该使用暂时性重定向。
  
在Flask中，重定向是通过 `flask.redirect(location, code=302)`这个函数来实现，`location`表示要重定向到的URL， 应该配合之前讲的 `url_for()` 函数来使用， code 表示采用了那个重定向，默认是302 既暂时性重定向，可以修改为301来实现永久性重定向。

```python
from flask import Flask,redirect, request, url_for


app = Flask(__name__)
app.debug = True

@app.route('/')
def index():

    return "hello index"

@app.route('/login/')
def login():

    return 'login Page'

@app.route('/profile/')
def profile():

    if request.args.get('name'):
        return '欢迎来到个人中心'
    else:
        # return redirect("/login/")
        return redirect(url_for('login'), code=302)

if __name__ == '__main__':
    app.run()
```

### 2.6 关于响应(Response)

试图函数的返回值会被自动转换为一个响应对象，Flask的转换逻辑如下：
- 如果返回的是一个合法的响应对象，则直接返回。「其实底层将这个字符串包装成了一个 `Response`对象。」
- 如果返回的是一个字符串， 那么Flask会重新创建一个`werkzeug.wrappers.Response`对象， Response将该字符串作为主体，状态码为200， MIME类型为：text/html， 然后返回Response对象。
- 如果返回的是一个元组，元组中的数据类型是(response.status.headers).status值会覆盖默认的200状态码， headers可以是一个列表或字典，作为额外的消息头。「元组的形式是(响应体,状态码, 头部信息)，也不一定三个都要，写两个也是可以的。返回的元组，在底层也是包装成了`Response`对象」
- 如果以上条件都不满足，Flask会假设返回值是一个合法的`wsgi`应用程序，并通过 `Response.force_type(rv, request.environ)`转换为一个请求对象。

#### 2.6.1 直接用Response创建

```python
from werkzeng.wrappers import Response

@app.route('/')
def index():
    resp = Response(response='about page', status=200, content_type='text/html;charset=utf-8')
    return resp

```

#### 自定义响应

- 必须继承自 Response类。
- 必须实现force_type(cls,rv,environ=None)
- 必须制定app.response_class 为你自定义的Response

```python
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


    if __name__ == '__main__':
        app.run()

```

## 第三章：模板 templates

### 3.1 模板预热

1. 在渲染模板的时候，默认会从项目目录下的 `templates`目录下查找模板。
2. 如果不想把模板文件放在`templates`目录下，可以在Flask初始化的时候指定`template_folder`的路径，来指定模板的路径


### 3.2 模板传参

1. 在使用`render_template`渲染模板的时候，可以传递关键字参数，以后直接在模板中使用就可以了
2. 如果你的参数过多，那么可以将所有的参数放到一个字典中，然后在传这个字典参数的时候，使用两个星号，将字典打散成关键字参数。

### 3.3 模板中使用url_for

模板中的`url_for`跟我们后台视图函数中的 `url_for`使用起来基本是一模一样的，也是传递视图函数的名字，也可以传递参数。使用的时候，需要在`url_for`左右加上花括号`{{ url_for }}`

### 4.3 模板中过滤器基本是使用

过滤器是通过管道符号( | )进行使用的，例如`{{ name | length}}`,将返回name的长度。过滤器相当于是一个函数，把当前的变量传入到过滤器中，然后获取器根据自己的功能，返回相应的值，之后再将结果渲染到页面，Jinja2中内置了很多过滤器，现在对一些常用的过滤器进行讲解

- abs(value): 返回一个数值的绝对值。





