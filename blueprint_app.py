from flask import Flask, render_template, url_for
from blueprint.user import user_bp
from blueprint.books import book_bp
from blueprint.cms import cms_bp


app = Flask(__name__)
app.config['SERVER_NAME'] = 'jd.com:5000'
app.debug = True
app.templates_auto_reload = True
app.register_blueprint(user_bp)
app.register_blueprint(book_bp)
app.register_blueprint(cms_bp)
# 用户模块
# 新闻模块
# 电影模块
# 读书模块


@app.route('/')
def index():

    print(url_for('user.profile'))
    return render_template('index.html')


if __name__ == '__main__':
  app.run()
 