import os

import requests, pytest, jsonpath
from xToolkit import xfile
from string import Template
from comm.gobal import gobal_v

# 1. 读取excel,并且把读出来的数据转换成列表

test_data_list = xfile.read("华测商城接口测试用例.xls").excel_to_dict(sheet=1)
print(test_data_list)

"""
最简单的框架封装思想!!!
问题：我还要写个购物车接口怎么办？ token 全局变量
订单接口 -- 商品接口信息？
结算接口 -- 订单信息？
xxx --  另外的接口信息呢？1500个接口
"""


# eval 这个函数，会自动按你的数据格式，格式化掉对应的数据 () []
# pytest有一个对应的方式 参数化机制
# 自动循环 DDT
@pytest.mark.parametrize("case_info", test_data_list)
def test_case_exec(case_info):  # 把这个列表传进来

    url = case_info["接口URL"]
    dic = gobal_v().show_dict()
    if "$" in url:
        url = Template(url).substitute(dic)

    rep = requests.request(
        url=url,
        method=case_info["请求方式"],
        params=eval(case_info["URL参数"]),
        data=eval(case_info["JSON参数"])
    )

    # 数据写入到对象中去
    if case_info['提取参数'] != None or case_info['提取参数'] != '':
        lst = jsonpath.jsonpath(rep.json(), '$..' + case_info['提取参数'])
        gobal_v().set_dict(case_info['提取参数'], lst[0])

    assert rep.status_code == case_info["预期状态码"]


if __name__ == '__main__':
    # pytest.main(['-vs','--capture=sys']) # pytest的启动命令!!
    pytest.main(['-s', '-v', '--capture=sys', 'Test_apiUser.py', '--clean-alluredir', '--alluredir=allure-results'])
    os.system(r"allure generate -c -o 测试报告")
