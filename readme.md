# 资产管理子系统
## 概述
主要功能：手动收集各大SRC平台主域名，通过程序自动处理以格式化存入数据库中，便于配合其它信息搜集工具进一步测试。

同时支持添加SRC备注信息，用于共享SRC接收范围、接收漏洞类型等信息，尽可能避免白帽子因信息差而走弯路浪费时间；众人拾柴火焰高，欢迎PR！
![](https://qiniu.xxf.world/pic/2024/04/14/7b0e631d-9ad0-46e8-85a9-87f5532d36a8.png)
![](https://qiniu.xxf.world/pic/2024/04/29/9ca685e9-a5b8-4282-a502-2309b366fa74.png)
## 使用
环境依赖
- mongodb

使用步骤
1. 将mongo连接信息填入default.ini.sample文件，并重命名为default.ini
2. 安装项目依赖 ```pip install -r requirements.txt```
3. 运行`python3 main.py`，asserts目录下的txt文件会自动被扫描并进入数据库
4. 运行`python3 main.py --purge`，会先清空数据库，再进行入库

添加资产: asserts目录下新增txt文件即可，第一行为企业名称，之后每一行为一个域名，重要的域名在结尾标记如`baidu.com -`

添加备注信息：在域名结尾行添加关键字`this is ps`后面的内容均不会被识别为域名，如上图所示

todo
- [x] 支持入库前清空数据库，以同步本地更改
- [x] 支持重要域名标记
- [x] 运行前检查环境
- [x] 自动添加索引
- [x] 支持src备注信息

docker快速搭建mongodb
`docker run -d -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=change_your_password --name mymongo mongo`