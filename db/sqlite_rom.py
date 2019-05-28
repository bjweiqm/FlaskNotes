from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///ceshi.db?check_same_thread=False', echo=True)
Base = declarative_base(engine)

# create table person(id int primary key autoincrement, name varcher(5), age int)
# 1.创建ORM模型，这个ORM模型必须继承自sqlalchemy给我们提供好的基类
class Person(Base):
    __tablename__ = 'person'  # 定义表的名字

    # 2.在这个ORM模型中创建一些属性，来跟表中的字段进行一一映射，这些属性必须是 sqlalchemy 给我们提供好的数据类型
    id = Column(Integer, primary_key=True, autoincrement=True)   # 定义列？
    name = Column(String(50))
    age = Column(Integer)

# 3.将创建好的数据类型，映射到数据库中
# Base.metadata.create_all()

# 增删改查操作 依赖于 SQLalchemy.orm 中的 sessionmaker
# 建立回话
Session = sessionmaker(bind=engine)
session = Session()


def insert_dl():
    # 添加一条数据
    # per = Person(id=1, name='zhangsan', age=20)
    # session.add(per)
    # 添加多条数据
    session.add_all(
        [
            Person(name='alex', age=12),
            Person(name='ata', age=30),
            Person(name='tuo', age=21),
            Person(name='ynh', age=18),
        ]
    )

def select_dl():
    name = session.query(Person).filter_by(name='tuo').first()
    print(type(name))
    print(name)
    print(name.age)



if __name__ == "__main__":
    select_dl()
    session.commit()