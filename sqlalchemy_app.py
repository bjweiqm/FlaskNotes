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

    def __repr__(self):
        return "<User(username: {}, id: {})>".format(self.username, self.id)


class Art(db.Model):
    __tablename__ = 'art'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    uid = db.Column(db.Integer, db.ForeignKey('user.id'))

    author = db.relationship("User", backref='art')


# db.drop_all()
# db.create_all()

# user = User(username='zhiliao')
# art = Art(title='title one')
# art.author = user
# db.session.add(art)
# db.session.commit()

# 查询一张表内数据，也可以用一下数据
# order_by
# filter
# filter_by
# group_by
# join
users = User.query.all()
users = User.query.order_by(User.id.desc()).all()

# 修改
# user = User.query.filter(User.id  == 3).first()
# user.username = 'tiedan'
# db.session.commit()
# 删除
# user = User.query.filter(User.id == 3).first()
# db.session.delete(user)
# db.session.commit()
print(users)


@app.route('/')
def index():
    return 'hello world'


if __name__ == "__main__":
    app.run(debug=True)
