from flask import Flask, render_template, request, views
from functools import wraps
app = Flask(__name__)


def login_required(func):
    # 编写装饰器 判断用户是否登录
    @wraps(func)
    def wrapper(*args, **kwargs):
        username = request.args.get('username')
        if username and username == 'zhiliao':
            return func(*args, **kwargs)
        else:
            return '请先登录'
    return wrapper


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/settings/')
@login_required
def setting():
    return '这是设置页面'


class ProfileView(views.View):
    decorators = [login_required]
    
    def dispatch_request(self):
        return '这是个人中心页面'


app.add_url_rule('/profile/', view_func=ProfileView.as_view('profile'))

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 

