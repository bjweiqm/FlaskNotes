#!/usr/bin/env python
# encoding: utf-8


from flask import Flask,render_template
import config
from ext import db


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

# 抽离到 ext 文件中。
# db = SQLAlchemy(app)

# 抽离到 models 文件中
# class User(db.Model):
#     __tablename__ = 'user'
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     username = db.Column(db.String(50), nullable=False)
#     email = db.Column(db.String(50), nullable=False)

#     def __repr__(self):
#         return "<User(id: {}, username: {}, email: {})>".format(
#             self.id, self.username, self.email
#         )

db.create_all()

@app.route('/')
def index():

    return 'hello !'

@app.route('/profile/')
def profile():
    pass


if __name__ == '__main__':
    app.run()
