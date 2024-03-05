import os
import pymongo
import yaml
from datetime import datetime
from module.database import conn_db

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
    db = conn_db("asserts")
    # 插入数据到数据库
    for company in companies:
        for domain in company['domains']:
            document = {
                'assert_name': company['name'],
                'domain': domain,
                'insert_time': datetime.now()
            }
            try:
                db.insert_one(document)
                print(f"插入记录完成{document}")
            except pymongo.errors.DuplicateKeyError:
                # 主键重复不处理
                print(f"记录重复{document}")

if __name__ == '__main__':
    txt_to_yaml()
    yaml_to_db()