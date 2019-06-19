# encoding:utf-8

# MySQL数据库链接方式
# DB_USERNAME = 'root'
# DB_PASSWORD = 'root'
# DB_HOST = '127.0.0.1'
# DB_PORT = '3306'
# DB_NAME = 'flask_demo'

# DB_URI = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8' %(
#     DB_USERNAME, DB_PASSWORD, DB_HOST, DB_PORT/DB_NAME
# )

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///tmp/test.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

