# flask-WTF

## 简介

Flask-WTF 是简化了 Flask-WTForms 操作的一个第三方库。WTForms表单的两个主要功能是验证用户提交数据的合法性以及渲染模板。当然包括一些其他功能：CSRF 保护，文件上传 等。安装Flask-WTF 也会默认安装 WTForms ，因此通过以下命令来安装 Flask-WTF 。
`pip install flask-wtf`

这个库一般有两个作用。第一个就是做表单验证， 把用户提交上来的数据进行验证是否合法。第二个就是做模板渲染

## 做表单验证

1. 自定义一个表单类， 继承自wtforms.Form类。
2. 定义好需要验证的字段， 字段的名字必须和模板中那些需要验证的input标签的name属性保持一致。
3. 在需要验证的字段上看需要指定好具体的数据类型。
4. 在相关的字段上，指定验证数据。
5. 以后再视图中，就只需要使用这个表单类的对象，并且把需要验证的数据，也就是request.form传给这个表单，以后调用 form.validate() 方法。如果返回True，那么代表用户输入的数据都是合法的，否则代表用户输入的数据是有问题的，如果验证失败了，那么可以通过form.errors来获取具体的错误信息。

实例代码
RegistForm中的代码

```python
from wtforms import Form, StringField
from wtforms.validators import Length,EqualTo


class RegistForm(Form):
    username = StringField(validators=[Length(min=3, max=10, message="长度错误")])
    password = StringField(validators=[Length(min=6, max=10)])
    password_repeat = StringField(validators=[Length(min=6, max=10), EqualTo('password')])
```

视图函数中的代码

```python
def regist():
    if request.method == 'GET':
        return render_template('regist.html')
    else:
        form = RegistForm(request.form)
        if form.validate():
            return 'success'
        else:
            print(form.errors)
            return 'fail'
```

### 常用验证器

1. Email: 验证上传数据是否为邮箱
2. EqualTo: 验证上传数据是否和另外一个字段相等， 常用的就是密码和确认密码两个字段是否相等
3. InputRequired: 原始数据的验证，如果不是特殊情况，应该使用InputTequired
4. Length: 长度限制，有min和max两个值进行限制
5. NumberRange: 数字的区间， 有min和max两个值限制，如果处在这两个数字之间则满足
6. Regexp: 自定义正则表达式
7. URL: 必须是URL的形式
8. UUID: 验证uuid。

### 自定义验证字段

如果想要对表单中的某个字段进行更细化的验证，那么可以针对这个字段进行单独的验证。步骤如下：

1. 定义一个方法，方法的名字规则是： `validate_字段名(self, filed)`
2. 在方法中，使用 filed.data 可以获取到这个字段的具体值
3. 如果数据满足条件，可以什么都不做。如果验证失败，那么应该抛出一个 `wtforms.validators.VaildationError` 的异常，并且把验证失败的信息传到这个异常类中

实例代码：

```python
captcha = StringField(validators=[Length(4, 4)])

def validate_captcha(self, field):
    # 用户提交的数据是存在 field.data 中
    if field.data != '1234':
        raise ValidationError('验证码错误！')
```

## 渲染模板

form 还可以渲染模板，让你少写了一部分代码。用不多

