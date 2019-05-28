# encoding: utf-8

from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean, DECIMAL, Enum, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import date
import enum



# 链接数据库
engine = create_engine('sqlite:///ceshi.db?check_same_thread=False', echo=True)
# 实例化官宣基础模型
Base = declarative_base(engine)
# 创建回话对象，打开回话对象
session = sessionmaker(bind=engine)()


class MyEnum(enum.Enum):

    python = 'python'
    flask = 'Flask'
    django = 'Django'


class Article(Base):
    # 创建数据库表名称
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    pric = Column(Float)
    is_delete = Column(Boolean)
    # decimal 接收两个参数， 第一个是所有数字的位数， 第二是小数点后的位数
    price = Column(DECIMAL(10, 4))
    # 枚举类型
    # tag = Column(Enum('python', 'php', 'java', 'c++'))
    tab = Column(Enum(MyEnum))
    # date 类型
    # create_date = Column(Date)
    # datetime 类型
    create_date = Column(DateTime)



# 检索所有继承Base的ORM对象，创建所有数据库表
Base.metadata.create_all()
# 删除所有数据库中所有的表
# Base.metadata.drop_all()


article = Article(pric=10.293, tab=MyEnum.python, create_date=date(2019, 5, 29, 12, 12, 12))
session.add(article)
session.commit()




