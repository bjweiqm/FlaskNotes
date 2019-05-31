# encoding:utf-8

from sqlalchemy import create_engine, String, Integer, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. 创建db链接
# 2. 生成基类
# 3. 实例话句柄
# 4. 操作数据库

engine = create_engine('sqlite:///self_db.db', echo=True)

Base = declarative_base(engine)
session = sessionmaker(engine)()





