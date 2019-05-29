from sqlalchemy import create_engine, Column, Integer, String, Float, func, and_, or_, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship, backref
import random

engine = create_engine('sqlite:///test2.db?check_same_thread=False', echo=True)

Base = declarative_base(engine)
sesson = sessionmaker(engine)()


class User(Base):
    __tablename__='user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)

    # articles = relationship("Article")
    # 指定针对 UserExtend 一对一关系。
    # extend = relationship('UserExtend', uselist=False)

    def __repr__(self):

        return "<User(username: {})>".format(self.username)


class UserExtend(Base):
    __tablename__='user_extend'
    id = Column(Integer, primary_key=True, autoincrement=True)
    school = Column(String(50), nullable=False)
    uid = Column(Integer, ForeignKey('user.id'))
    # 一对一关系。
    user = relationship("User", backref=backref("extend", uselist=False) )

    def __repr__(self):
        return "<UserExtend(shool: {})>".format(self.school)


class Article(Base):
    __tablename__='article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    content = Column(Text, nullable=False)

    uid = Column(Integer, ForeignKey("user.id", ondelete="RESTRICT"))

    author = relationship("User", backref="article")

    def __repr__(self):
        return "<Article(title: {}, content: {})>".format(self.title, self.content)


Base.metadata.drop_all()
Base.metadata.create_all()

# 一对一

user = User(username='zihliao')
extend = UserExtend(school='qing hua')
user.extend = extend
sesson.add(user)


# # 从article中往user中添加数据
# user = User(username='zhiliao')

# article = Article(title='abc', content='123')
# article.author = user

# sesson.add(article)

# 从user中往article中添加数据
# user = User(username='zhiliao')

# article = Article(title='abc', content='123')
# article2 = Article(title='efd', content='456')
 
# user.article.append(article)
# user.article.append(article2)

# sesson.add(user)

sesson.commit()

