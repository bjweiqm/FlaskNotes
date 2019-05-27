from flask import Flask, render_template
from blueprint.user import user_bp
from blueprint.books import book_bp


app = Flask(__name__)
app.config['SERVER_NAME'] = 'dl.com:8000'
# app.templates_auto_reload = True
app.register_blueprint(user_bp)
app.register_blueprint(book_bp)

# 用户模块
# 新闻模块
# 电影模块
# 读书模块


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 