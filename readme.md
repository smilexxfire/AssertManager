# 资产管理子系统
## 概述
主要功能：**手动收集各大SRC平台主域名**，通过程序自动处理以格式化存入数据库中，便于配合其它信息搜集工具进一步测试。

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

添加资产: asserts目录下新增txt文件即可，第一行为企业名称，之后每一行为一个域名

添加备注信息：在文本末尾添加关键字`this is ps`后面的内容均不会被识别为域名，如上图所示

docker快速搭建mongodb
`docker run -d -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=admin -e MONGO_INITDB_ROOT_PASSWORD=change_your_password --name mymongo mongo`
## 查询
支持通过模糊查询assert_name获取所有相关子域

`python search.py --assert_name 百度`
![](https://qiniu.xxf.world/pic/2024/10/04/445fe807-8fd7-4d00-bd8b-c447e5dc2ed0.png)

## TODO
- [x] 资产入库
- [x] 资产持久化
- [x] 支持入库前清空数据库，以同步本地更改
- [x] 支持重要域名标记
- [x] 运行前检查环境
- [x] 自动添加索引
- [x] 支持src备注信息
- [x] 模糊查询
## 已收录资产
- [51信用卡](./asserts/51xinyongka.txt)
- [58集团](./asserts/58.txt)
- [阿里巴巴](./asserts/ali.txt)
- [安恒](./asserts/anheng.txt)
- [百度](./asserts/baidu.txt)
- [上海贝锐](./asserts/beirui.txt)
- [北京北森云计算股份有限公司](./asserts/beisengyun.txt)
- [字节跳动](./asserts/bytedance.txt)
- [安徽省刀锋网络科技有限公司](./asserts/daofeng.txt)
- [嘀嗒出行](./asserts/didachuxing)
- [滴滴](./asserts/didi.txt)
- [丁香园](./asserts/dingxiangyuan.txt)
- [度小满](./asserts/duxiaoman.txt)
- [北京粉笔蓝天科技有限公司](./asserts/fenbilantian.txt)
- [上海付费通信息服务有限公司](./asserts/fufeitong.txt)
- [国海证劵](./asserts/guohaizhengjuan.txt)
- [上海合合信息科技股份有限公司](./asserts/hehe.txt)
- [环球时报](./asserts/huanqiushibao.txt)
- [华为](./asserts/huawei.txt)
- [华住](./asserts/huazhu.txt)
- [货讯通科技](./asserts/huoxuntong.txt)
- [京东](./asserts/jd.txt)
- [快手](./asserts/kuaishou.txt)
- [联想](./asserts/lenovo.txt)
- [理想汽车](./asserts/lixiang.txt)
- [麦当劳](./asserts/mdl.txt)
- [美团](./asserts/meituan.txt)
- [陌陌](./asserts/momo.txt)
- [oppo](./asserts/oppo.txt)
- [paypal中国](./asserts/paypal_cn.txt)
- [平安科技](./asserts/pingan.txt)
- [人民教育出版社](./asserts/renminjiaoyu.txt)
- [shein](./asserts/shein.txt)
- [申通](./asserts/shentong.txt)
- [水滴公司](./asserts/shuidi.txt)
- [顺丰](./asserts/shunfeng.txt)
- [搜狐](./asserts/souhu.txt)
- [腾讯](./asserts/tencent.txt)
- [同程旅行](./asserts/tongcheng.txt)
- [vivo](./asserts/vivo.txt)
- [小米](./asserts/xiaomi.txt)
- [携程旅行](./asserts/xiecheng.txt)
- [信也科技集团](./asserts/xinyekeji.txt)
- [阳光保险](./asserts/yangguangbaoxian.txt)
- [北京易车](./asserts/yiche.txt)
- [银联](./asserts/yinlian.txt)
- [翼支付](./asserts/yizhifu.txt)
- [圆通](./asserts/yuantong.txt)
- [知识星球](./asserts/zsxq.txt)
