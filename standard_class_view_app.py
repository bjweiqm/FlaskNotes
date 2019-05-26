from flask import Flask, render_template, views, url_for,jsonify
app = Flask(__name__)

# 有几个url需要返回json数据
# 有几个url 返回的变量相同

@app.route('/')
def index():
    return render_template('index.html')


class JSONView(views.View):
    def get_data(self):
        raise NotImplementedError

    def dispatch_request(self):
        return jsonify(self.get_data())

class ListViews(JSONView):

    def get_data(self):
        return {
            'username': 'zhiliao',
            'password': 111111,
        }


class ADSView(views.View):

    def __init__(self):
        super(ADSView, self).__init__()
        self.context = {
            'ads': '今年过节不收礼啊'
        }

class LoginView(ADSView):
    
    def dispatch_request(self):
        return render_template('class_view/login.html', **self.context)


class RegistView(ADSView):

    def dispatch_request(self):
        return render_template('class_view/regist.html', **self.context)

class ListView(views.View):

    def dispatch_request(self):
        return 'list view'

app.add_url_rule('/list/', view_func=ListView.as_view('list'))
app.add_url_rule('/lists/', view_func=ListViews.as_view('lists'))
app.add_url_rule('/login/', view_func=LoginView.as_view('login'))
app.add_url_rule('/regist/', view_func=RegistView.as_view('regist'))

with app.test_request_context():
    print(url_for('list'))

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 