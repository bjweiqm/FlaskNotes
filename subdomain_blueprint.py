#!/usr/bin/env python
# encoding: utf-8


from flask import Flask,render_template
from blueprint.tools import tools_bp


app = Flask(__name__)
app.config['SERVER_NAME'] = 'jd.com:5000'
app.debug=True
app.templates_auto_reload=True
app.register_blueprint(tools_bp)


@app.route('/')
def index():

    return render_template('index.html')


if __name__ == '__main__':
    app.run()
