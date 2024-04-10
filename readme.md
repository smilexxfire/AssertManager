# 资产管理子系统
## 概述
主要功能：手动收集各大SRC平台主域名，通过程序自动处理以格式化存入数据库中，便于配合其它信息搜集工具进一步测试。

## 使用
环境依赖
- mongo

使用步骤
1. 将mongo连接信息填入default.ini.sample文件，并重命名为default.ini
2. 安装项目依赖 ```pip install -r requirements.txt```
3. 运行`python3 main.py`，asserts目录下的txt文件会自动被扫描并进入数据库
4. 运行`python3 main.py --purge`，会先清空数据库，再进行入库

添加资产: asserts目录下新增txt文件即可，第一行为企业名称，之后每一行为一个域名，重要的域名在结尾标记如`baidu.com -`

todo
- [x] 支持入库前清空数据库，以同步本地更改
- [x] 支持重要域名标记
- [x] 运行前检查环境
- [x] 自动添加索引
