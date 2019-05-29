from sqlalchemy import create_engine, Column, Integer, String, Float, func, and_, or_, ForeignKey, Text, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship
import random

engine = create_engine('sqlite:///test3.db?check_same_thread=False', echo=True)

Base = declarative_base(engine)
sesson = sessionmaker(engine)()
article_tag = Table(
    'create_tag',
    Base.metadata,
    Column('article_id', Integer, ForeignKey('article.id'), primary_key=True),
    Column('tag_id', Integer, ForeignKey('tag.id'), primary_key=True)
)

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)

    # tags = relationship('Tag', backref='articles', secondary=article_tag)

    def __repr__(self):
        return "<Article(title: {})>".format(self.title)


class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    articles = relationship('Article', backref='tags', secondary=article_tag)

    def __repr__(self):
        return "<Tag(name: {})>".format(self.name)



# 1. 先把两个需要做多对多的模型定义出来
# 2. 只用Table定义一个中间表，中间表一般就是包含两个模型的外键字段就可以了， 并且让他们两个来作为一个 复合主键
# 3. 在两个需要做多对多的模型中随便选择一个模型， 定义一个 relationship 属性，来绑定三者之间的关系，在使用 relationship 的时候，需要传入一个 secondary=中间件。


# Base.metadata.drop_all()
# Base.metadata.create_all()

# title1 = Article(title='title1')
# title2 = Article(title='title2')

# tag1 = Tag(name='tag1')
# tag2 = Tag(name='tag2')

# title1.tags.append(tag1)
# title1.tags.append(tag2)

# title2.tags.append(tag1)
# title2.tags.append(tag2)

# sesson.add(title1)
# sesson.add(title2)

# article = sesson.query(Article).first()
# print(article.tags)

tag = sesson.query(Tag).first()
print(tag.articles)

sesson.commit()
