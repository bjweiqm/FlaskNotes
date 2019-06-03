# encoding: utf-8

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# 链接数据库
engine = create_engine('sqlite:///test5.db', echo=True)
# 创建基类
Base = declarative_base(bind=engine)
session = sessionmaker(engine)()


# 实例化数据库
class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    city = Column(String(50), nullable=False)
    age = Column(Integer, default=0)

    def __repr__(self):
        return "<User(username: {}, city: {}, age: {})>".format(
            self.username,
            self.city,
            self.age
        )

# 删除数据库内所有表
# Base.metadata.drop_all()
# 在数据库中创建定义的所有的表
# Base.metadata.create_all()


# 插入数据
# session.add_all([
#     User(username='李A', city='长沙', age=18),
#     User(username='王B', city='长沙', age=18),
#     User(username='赵C', city='北京', age=18),
#     User(username='张D', city='长沙', age=20)

# ])



# 提交数据
# session.commit()

# 寻找和李A这个人在同一个城市，并且是同龄的人
# 第一种方法, 需要两条SQL语句。
# user = session.query(User).filter(User.username == '李A').first()
# users = session.query(User).filter(User.city == user.city, User.age == user.age).all()
# print(users)

# 第二种方式, 能够提升查询性能。
stmt = session.query(User.city.label('city'), User.age.label('age')).filter(User.username=='李A').subquery()

result = session.query(User).filter(User.city == stmt.c.city, User.age == stmt.c.age).all()
print(result)

