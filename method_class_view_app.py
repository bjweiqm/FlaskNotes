from flask import Flask, render_template, views,request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# 开始使用类视图函数
class LoginView(views.MethodView):

    def __render(self, error=None):
        return render_template('class_view/login.html', error=error)

    def get(self, error=None):
        return self.__render()

    def post(self):

        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'zhiliao' and password == '111111':
            return '登录成功'
        else:
            error = '用户名或密码错误'
            return self.__render('class_view/login.html', error=error)



# 注册视图函数
app.add_url_rule('/login/', view_func=LoginView.as_view('login'))
app.add_url_rule('/log/', view_func=LoginView.as_view('loge'))

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 