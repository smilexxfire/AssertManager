import pymongo
from pymongo import MongoClient
from utils.tools import *

class ConnMongo(object):
    username = read_ini_config("mongodb", "username")
    password = read_ini_config("mongodb", "password")
    host = read_ini_config("mongodb", "host")
    port = read_ini_config("mongodb", "port")
    def __new__(self):
        if not hasattr(self, 'instance'):
            uri = f'mongodb://{self.username}:{self.password}@{self.host}:{self.port}' \
                if self.username and self.password else f'mongodb://{self.host}:{self.port}'
            self.instance = super(ConnMongo, self).__new__(self)
            self.instance.conn = MongoClient(uri)
        return self.instance


def conn_db(collection):
    db_name = read_ini_config("mongodb", "db")
    conn = ConnMongo().conn
    if db_name:
        return conn[db_name][collection]

def insert_to_db(data):
    # 插入数据库
    try:
        db = conn_db("asserts")
        result = db.insert_many(data, ordered=False)
    except pymongo.errors.BulkWriteError as e:
        for error in e.details['writeErrors']:
            if error['code'] == 11000:  # E11000 duplicate key error collection，忽略重复主键错误
                pass
                # print(f"Ignoring duplicate key error for document with _id {error['op']['_id']}")
            else:
                raise  # 如果不是重复主键错误，重新抛出异常

def create_index():
    try:
        db = conn_db("asserts")
        # 创建索引，并设置 background 参数为 True
        db.create_index([("domain", pymongo.ASCENDING)])
        print("创建索引...")

    except pymongo.errors.OperationFailure as e:
        # 检查错误消息是否为索引已存在的错误
        if "An existing index has the same name as the requested index" in str(e):
            print("索引已存在...")
        else:
            # 如果错误消息不是索引已存在的错误，则重新引发异常
            raise e
    except Exception as e:
        print("数据库连接失败")

if __name__ == '__main__':
    db = conn_db("asserts")
    results = db.find()
    for rs in results:
        print(rs)