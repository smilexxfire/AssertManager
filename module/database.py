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

# db = conn_db("asserts")
# results = db.find()
# for rs in results:
#     print(rs)