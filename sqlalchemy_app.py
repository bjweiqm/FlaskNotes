from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)


class Art(db.Model):
    __tablename__ = 'art'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    uid = db.Column(db.Integer, db.ForeignKey('user.id'))

    author = db.relationship("User", backref='art')


db.drop_all()
db.create_all()

user = User(username='zhiliao')
art = Art(title='title one')
art.author = user
db.session.add(art)
db.session.commit()


@app.route('/')
def index():
    return 'hello world'


if __name__ == "__main__":
    app.run(debug=True)
