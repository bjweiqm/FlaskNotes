from sqlalchemy import create_engine

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'first_sqlalchemy'
USERNAME = 'root'
PASSWORD = 'root'
DB_URL = 'mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8'.format(
    username=USERNAME, password=PASSWORD, host=HOSTNAME, port=PORT, db=DATABASE
)


engine = create_engine(DB_URL)

# 判断是否连接成功
conn = engine.connect()

conn.execute('select 1')
