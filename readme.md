# 资产管理子系统
## 概述
主要功能：将手动收集的各大SRC平台主域名按照规定格式存入数据库中，便于进行后续的信息搜集工作

## 使用
环境依赖
- mongo

使用步骤
1. 在mongodb中依次运行mongo.db文件中的两条语句，以创建索引
2. 将mongo连接信息填入default.ini.sample文件
3. 将default.ini.sample重命名为default.ini
4. 安装项目依赖 ```pip install -r requirements.txt```
5. 运行main.py，asserts目录下的txt文件会自动被扫描并进入数据库

添加资产: asserts目录下新增txt文件即可，第一行为企业名称，之后每一行为一个域名