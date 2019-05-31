from sqlalchemy import create_engine, Column, Integer, String, Float, func, and_, or_, ForeignKey, Text, Table, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship, backref
import random, datetime

engine = create_engine('sqlite:///test4.db', echo=True)

Base = declarative_base(engine)
session = sessionmaker(engine)()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)

    def __repr__(self):
        return "<User(id: {}, username: {})>".format(self.id, self.username)


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    create_time = Column(DateTime, nullable=False, default=datetime.datetime.now)
    uid = Column(Integer, ForeignKey('user.id'))
    # 写在多的一方， 懒加载 lazy='dynamic'
    author = relationship('User', backref=backref('article', lazy='dynamic'))

    def __repr__(self):

        return "<Article(id: {}, title: {}, create_time: {})>".format(
            self.id, self.title, self.create_time
        )

def t4st():
    Base.metadata.drop_all()
    Base.metadata.create_all()


    user = User(username='zhiliao')

    for x in range(100):
        article = Article(title="title {}".format(x))
        article.author = user
        # article 不是一个列表，不能使用append添加数据
        # article.author.append(user)
        session.add(article)

user = session.query(User).first()
# 是一个query对象
# print(user.article)
# print(user.article.filter(Article.id > 50).all())
# 因为是AppendQuery，所以可以继续追加数据进去
articles = Article(title='title 100')
user.article.append(articles)
session.commit()


