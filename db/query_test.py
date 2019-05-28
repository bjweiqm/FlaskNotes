from sqlalchemy import create_engine, Column, Integer, String, Float, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import random

engine = create_engine('sqlite:///test.db?check_same_thread=False', echo=True)

Base = declarative_base(engine)
sesson = sessionmaker(engine)()



class Article(Base):

    __tablename__ = 'article'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)

    def __repr__(self):
        return "<Article(title:{title}, price:{price})>".format(title=self.title, price=self.price)


# Base.metadata.drop_all()
# Base.metadata.create_all()

# for x in range(50):
#     article = Article(title='title%s' % x, price=random.randint(50, 300))
#     sesson.add(article)

# articles = sesson.query(Article.title, Article.price).all()
# articles = sesson.query(Article).all()

# for i in articles:
#     print(i)

# 聚合函数
result = sesson.query(func.count(Article.id)).first()
print(result)


sesson.commit()
