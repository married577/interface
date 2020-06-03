# 检查点需要手动json转，url：http://www.bejson.com/jsonviewernew/

# 前言
1.环境准备：
- python3.6
- requests
- pymysql
- xlrd
- openpyxl

2.目前实现的功能：
- 封装requests请求方法
- 在excel填写接口请求参数
- 运行完后，重新生成一个excel报告，结果写入excel
- 用unittest+ddt数据驱动模式执行
- HTMLTestRunner生成可视化的html报告
- 对于没有关联的单个接口请求是可以批量执行的
- logging日志文件

3.目前已知的缺陷：
- 接口请求参数名有重复的，目前未处理，如key1=value1&key1=value2,两个key都一样，这种需要用元组存储，目前暂时未判断
- 生成的excel样式未处理，后期慢慢优化样式

3.需要优化的地方
- 返回数据是时时的接口，断言处理
- 删除无用的代码
- excle有效数据行数取值

4.目前已有的
- 对于没有关联的单个接口请求，是通过excle管理case批量执行的
- 没有关联的接口，是在某个文件单独执行