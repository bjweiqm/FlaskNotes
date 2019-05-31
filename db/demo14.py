from sqlalchemy import create_engine, Column, Integer, String, Float, func, and_, or_, ForeignKey, Text, Table, DateTime, Enum
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
    age = Column(Integer, default=0)
    gender = Column(Enum('male', 'female', 'secret'), default='male')

    def __repr__(self):
        return "<User(username: {}, age: {}, gender: {})>".format(self.username, self.age, self.gender)


def init_test():
    Base.metadata.drop_all()
    Base.metadata.create_all()


    session.add_all(
        [
            User(username="王武", age= 17, gender='male'),
            User(username="赵柳", age= 17, gender='male'),
            User(username="张三", age= 18, gender='female'),
            User(username="王大武", age= 19, gender='female'),
            User(username="知了", age= 20, gender='female'),
        ]
    )

    session.commit()

# 各年龄段的人数 group_by()
# user = session.query(User.age, func.count(User.id)).group_by(User.age).all()
# print(user)

# having 
user = session.query(User.age, func.count(User.id)).group_by(User.age).having(User.age < 18).all()
print(user)



