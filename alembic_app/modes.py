from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///tmp/test1.db', echo=True)

Base = declarative_base(engine)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)

    def __repr__(self):
        return "<User(id: {}, username: {})>".format(self.id, self.username)

# 初始化alembic仓库  alembic init alembic_name
# 创建模型 本文件是在创建数据库模型
# 修改配置文件 alembic.ini 中的链接方式 sqlalchemy.url = sqlite:///tmp/test1.db。 修改env.py 中的 target_metadata = Base.metadata
# 生成迁移脚本 alembic revision --autogenerate -m 'first submit'
# 映射到数据中 alembic upgrade head 
