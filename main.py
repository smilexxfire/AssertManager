import os
import pymongo
from datetime import datetime
from module.database import conn_db, insert_to_db, create_index, insert_to_comment_db
import re
import sys

def is_valid_ipv4(address):
    pattern = r'^(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.' \
              r'(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.' \
              r'(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.' \
              r'(?:25[0-5]|2[0-4]\d|[01]?\d\d?)$'
    return bool(re.match(pattern, address))
# 定义一个函数来执行模糊查询
def fuzzy_search(substring, strings):
    return [s for s in strings if substring.lower() in s.lower()]

def format_all_to_db(input_directory):
    # 获取输入目录下所有的 domains.txt 文件
    input_files = [f for f in os.listdir(input_directory) if f.endswith(".txt")]
    insert_data = list()
    comment_data = list()

    for input_file in input_files:
        # 构建输入文件的完整路径
        input_file_path = os.path.join(input_directory, input_file)

        # 读取企业名称和域名信息
        with open(input_file_path, 'r', encoding="utf8") as file:
            lines = [line for line in file.readlines()]
            company_name = lines[0].strip()
            # 检查是否存在备注内容
            search_results = fuzzy_search("this is ps", lines)
            if search_results:  # 存在则截断
                index = lines.index(search_results[0])
                comment = "".join(lines[index + 1:])
                lines = lines[:index]
                comment_data.append({"assert_name": company_name, "comment": comment})
            domains = [line.strip() for line in lines[1:]]
            for domain in domains:
                if is_valid_ipv4(domain):   # 忽略ipv4
                    continue
                # 删除字符*
                domain = domain.replace("*.", "")
                document = {
                    'assert_name': company_name,
                    'domain': domain,
                    'insert_time': datetime.now()
                }
                if domain.endswith(" -"):
                    domain = domain.strip(" -")
                    document["is_important"] = 1
                    document["domain"] = domain
                insert_data.append(document)
    # 插入数据库
    insert_to_db(insert_data)
    insert_to_comment_db(comment_data)

def txt_to_db():
    # 示例用法
    input_dir = "asserts"
    format_all_to_db(input_dir)

def check():
    # 检查配置文件是否存在
    print("检查配置文件是否存在...")
    if not os.path.exists("default.ini"):
        print("配置文件不存在，请编写default.ini文件")
        sys.exit(1)
    # 检查数据库连接是否正常
    print("检查数据库连接...")
    db = conn_db("asserts")
    db = conn_db("comments")
    print("检查通过 enjoy it...")

if __name__ == '__main__':
    check()
    if "--purge" in sys.argv:
        db = conn_db("asserts")
        db.delete_many({})
        db = conn_db("comments")
        db.delete_many({})
    # 为数据库创建索引
    create_index("asserts", "domain")
    create_index("comments", "assert_name")
    # 入库
    txt_to_db()
    print("资产已全部入库...")
