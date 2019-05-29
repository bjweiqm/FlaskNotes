from sqlalchemy import create_engine, Column, Integer, String, Float, func, and_, or_
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
# result = sesson.query(func.count(Article.id)).first()
# print(result)

# 1. equal
# art  = sesson.query(Article).filter(Article.title == 'title0').first()
# print(art)

# 2. not  equal 
# art = sesson.query(Article).filter(Article.title != 'title0').all()
# print(art)

# 3. like 模糊查询 ilike  不区分大小写
# art = sesson.query(Article).filter(Article.title.like('title%')).all()
# print(art)

# 4. in 
# art = sesson.query(Article).filter(Article.title.in_(['title1', 'title2'])).all()
# print(art)


# 5. not in 两种实现方式， ~ 
# art = sesson.query(Article).filter(Article.title.notin_(['title1', 'title2', 'title3'])).all()
# print(art)
# art = sesson.query(Article).filter(~Article.title.in_(['title1', 'title2', 'title3'])).all()
# print(art)

# 6. is null | is not null
# art = sesson.query(Article).filter(Article.title == None).all()

# 7. and
# art = sesson.query(Article).filter(and_(Article.title='title01', Article.id=5)).all()

# 8. or
# art = sesson.query(Article).filter(or_(Article.title == 'title2', Article.id = 3)).all()
# print(art)




sesson.commit()
