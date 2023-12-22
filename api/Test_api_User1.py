import os

import pytest
import requests
import jsonpath
from xToolkit import xfile
from string import Template

from comm.gobal import gobal_v

hc_api_shop = xfile.read("G:\\zidonghua\\华测商城接口测试用例.xls").excel_to_dict(sheet=1)
print(hc_api_shop)


@pytest.mark.parametrize("hc_info", hc_api_shop)
def excel_list(hc_info):
    res = requests.request(
        url=hc_info["接口URL"],
        method=hc_info["请求方式"],
        parmars=eval(hc_info["URL参数"]),
        data=eval(hc_info["JSON参数"])
    )

    assert res.status_code == hc_info["预期状态码"]


if __name__ == '__main__':
    pytest.main(['-s','-v', '--capture=sys'])  # ,'Test_apiUser.py','--clean-alluredir','--alluredir=allure-results'
    # os.system(r"allure generate -c -o 测试报告")
