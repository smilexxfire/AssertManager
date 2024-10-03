# -*- coding: UTF-8 -*-
'''
@Project ：assertManager 
@File    ：search.py
@IDE     ：PyCharm 
@Author  ：smilexxfire
@Email   : xxf.world@gmail.com
@Date    ：2024/10/4 1:00 
@Comment ： 通过模糊查询assert_name获取所有主域名
'''
import argparse

from module.database import conn_db
description = '''
Example：python search.py --assert_name 百度
'''
parser = argparse.ArgumentParser(description=description)
parser.add_argument('--assert_name', help='资产名称，模糊搜索', required=True)
args = parser.parse_args()

assert_name = args.assert_name
db = conn_db("asserts")
# i表示忽略大小写
query = {"assert_name": {"$regex": assert_name, "$options": "i"}}
results = db.find(query)
for result in results:
    print(result['domain'])