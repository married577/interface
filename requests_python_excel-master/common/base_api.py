# coding:utf-8
import json
import requests
from common.readexcel import ExcelUtil
from common.writeexcel import copy_excel, Write_excel
from common.other_case import excle_save

# 从登录返回数据中取token并填入excle的headers中
excle_save()


def send_requests(s, testdata):
    # 封装requests请求
    method = testdata["method"]
    url = testdata["url"]

    # url后面的params参数
    try:
        params = eval(testdata["params"])
    except:
        params = None

    # post请求body类型  json就填json，其他的就填data
    type = testdata["type"]

    test_nub = testdata['id']
    print("*******正在执行用例：-----  %s  ----**********" % test_nub)

    # 请求头部headers
    try:
        headers = eval(testdata["headers"])
        print("请求头部：%s" % headers)
    except:
        headers = None
        print("请求头部：%s" % headers)

    print("请求方式：%s" % method)
    print("请求url： %s" % url)

    # post请求body内容
    try:
        bodydata = eval(testdata["body"])
    except:
        bodydata = {}

    # 判断传data数据还是json，并打印接口信息
    if type == "data":
        body = bodydata
    elif type == "json":
        body = json.dumps(bodydata)
    else:
        body = bodydata
    if method == "post":
        print("post请求的body类型为：%s" % type)
        print("post请求的body内容为：%s" % body)
    elif method == "get":
        print("get请求的params类型为：%s" % type)
        print("get请求的params内容为：%s" % params)

    verify = False
    res = {}   # 接受返回数据

    try:
        r = s.request(method=method, url=url, params=params, headers=headers, data=body, verify=verify)
        print("页面返回信息：%s" % r.content.decode("utf-8"))
        res['id'] = testdata['id']
        res['rowNum'] = testdata['rowNum']

        # 状态码转成str
        res["statuscode"] = str(r.status_code)
        res["text"] = r.content.decode("utf-8")

        # 接口请求时间转str
        res["times"] = str(r.elapsed.total_seconds())

        if res["statuscode"] != "200":
            res["error"] = res["text"]
        else:
            res["error"] = ""
        res["msg"] = ""
        if testdata["checkpoint"] in res["text"]:
            res["result"] = "pass"
            print("用例测试结果:   %s---->%s" % (test_nub, res["result"]))
        else:
            res["result"] = "fail"
        return res
    except Exception as msg:
        res["msg"] = str(msg)
        return res


def wirte_result(result, filename="result.xlsx"):
    # 返回结果的行数row_nub
    row_nub = result['rowNum']
    # 写入statuscode
    wt = Write_excel(filename)

    # 写入返回状态码statuscode,第8列
    wt.write(row_nub, 8, result['statuscode'])

    # 耗时
    wt.write(row_nub, 9, result['times'])

    # 状态码非200时的返回信息
    wt.write(row_nub, 10, result['error'])

    wt.write(row_nub, 12, result['result'])

    # 抛异常
    wt.write(row_nub, 13, result['msg'])


if __name__ == "__main__":
    data = ExcelUtil("debug_api.xlsx").dict_data()
    print(data[0])
    s = requests.session()
    res = send_requests(s, data[0])
    copy_excel("debug_api.xlsx", "result.xlsx")
    wirte_result(res, filename="result.xlsx")
