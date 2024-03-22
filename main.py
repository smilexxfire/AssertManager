import os
import pymongo
import yaml
from datetime import datetime
from module.database import conn_db
import re
def is_valid_ipv4(address):
    pattern = r'^(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.' \
              r'(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.' \
              r'(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.' \
              r'(?:25[0-5]|2[0-4]\d|[01]?\d\d?)$'
    return bool(re.match(pattern, address))

def format_all_to_single_yaml(input_directory, output_file):
    # 获取输入目录下所有的 domains.txt 文件
    input_files = [f for f in os.listdir(input_directory) if f.endswith(".txt")]

    data = {'companies': []}

    for input_file in input_files:
        # 构建输入文件的完整路径
        input_file_path = os.path.join(input_directory, input_file)

        # 读取企业名称和域名信息
        with open(input_file_path, 'r') as file:
            lines = file.readlines()
            company_name = lines[0].strip()
            domains = [line.strip() for line in lines[1:]]

        # 构建当前企业的数据结构
        company_data = {'name': company_name, 'domains': domains}
        data['companies'].append(company_data)

    # 写入单个 YAML 文件
    with open(output_file, 'w', encoding="utf8") as file:
        yaml.dump(data, file, allow_unicode=True)

def txt_to_yaml():
    # 示例用法
    input_dir = "asserts"
    output_yaml_file = ("asserts/output.yaml")
    format_all_to_single_yaml(input_dir, output_yaml_file)

def yaml_to_db():
    # 读取 YAML 文件
    with open('asserts/output.yaml', 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
    # 获取数据
    companies = data.get('companies', [])
    # 插入数据到数据库
    insert_list = list()
    for company in companies:
        for domain in company['domains']:
            # 不添加ipv4
            if is_valid_ipv4(domain):
                continue
            document = {
                'assert_name': company['name'],
                'domain': domain,
                'insert_time': datetime.now()
            }
            insert_list.append(document)
    try:
        db = conn_db("asserts")
        db.insert_many(insert_list, ordered=False)
    except pymongo.errors.BulkWriteError as e:
        for error in e.details['writeErrors']:
            if error['code'] == 11000:  # E11000 duplicate key error collection，忽略重复主键错误
                pass
                # print(f"Ignoring duplicate key error for document with _id {error['op']['_id']}")
            else:
                raise  # 如果不是重复主键错误，重新抛出异常

if __name__ == '__main__':
    txt_to_yaml()
    yaml_to_db()