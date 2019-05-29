from sqlalchemy import create_engine, Column, Integer, String, Float, func, and_, or_, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship
import random

engine = create_engine('sqlite:///test1.db?check_same_thread=False', echo=True)

Base = declarative_base(engine)
sesson = sessionmaker(engine)()


class User(Base):
    __tablename__='user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)

    # articles = relationship("Article")

    def __repr__(self):

        return "<User(username: {})>".format(self.username)


class Article(Base):
    __tablename__='article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    content = Column(Text, nullable=False)

    uid = Column(Integer, ForeignKey("user.id", ondelete="RESTRICT"))

    author = relationship("User", backref="article")

    def __repr__(self):
        return "<Article(title: {}, content: {})>".format(self.title, self.content)



u = sesson.query(User).first()
print(u.articles)

sesson.commit()



# Base.metadata.create_all()

# sesson.add_all([
#     User(username='zhiliao'),
#     User(username='alex')
# ])

# sesson.add_all([
#     Article(title='abc', content='123', uid=1),
#     Article(title='abce', content='1234', uid=2),
#     Article(title='abcd', content='1235', uid=1),
# ])

# 现在基于两个表，分别为 user 和 article ，他们俩之间存在一个外键关系；
# article = sesson.query(Article).first()
# uid = article.uid
# print(article)
# user = sesson.query(User).get(uid)
# print(user)

# article = sesson.query(Article).first()
# au = article.author
# print(au.username)


# user = sesson.query(User).first()
# usr = sesson.query(User).first()
# print(usr)
# art = user.articles
# print(art)
