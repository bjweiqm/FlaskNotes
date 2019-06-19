#!/usr/bin/env python
# encoding: utf-8


from flask import Flask,render_template, request
from forms import RegistForm, LoginForm, SettingsForm
import config



app = Flask(__name__)
app.config.from_object(config)


@app.route('/', methods=['GET', 'POST'])
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
        

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        form = LoginForm(request.form)
        if form.validate():
            return '成功'
        else:
            print(form.errors)
            return 'fild'


@app.route('/strings/', methods=['GET', 'POST'])
def strings():
    if request.method == 'GET':
        form = SettingsForm()
        return render_template('settings.html', form=form)
    else:
        string = SettingsForm(request.form)



if __name__ == '__main__':
    app.run()
