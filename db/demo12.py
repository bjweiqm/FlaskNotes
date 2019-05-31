from sqlalchemy import create_engine, Column, Integer, String, Float, func, and_, or_, ForeignKey, Text, Table, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship
import random, datetime

engine = create_engine('sqlite:///test1.db', echo=True)

Base = declarative_base(engine)
session = sessionmaker(engine)()



class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50))
    create_time = Column(DateTime, default=datetime.datetime.now)

    def __repr__(self):

        return "<Article(id: {}, title: {}, create_time: {})>".format(
            self.id, self.title, self.create_time
        )

def test_():
    Base.metadata.drop_all()
    Base.metadata.create_all()


    for x in range(100):
        title = 'title {}'.format(x)
        article = Article(title=title)
        session.add(article)

# article = session.query(Article).all()
# article = session.query(Article).limit(10).all()
# article = session.query(Article).offset(10).limit(10).all()
# article = session.query(Article).order_by(Article.id.desc()).offset(10).limit(10).all()
# article = session.query(Article).order_by(Article.id.desc()).slice(0, 10).all()
article = session.query(Article).order_by(Article.id.desc())[0: 10]
print(article)

session.commit()