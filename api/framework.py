from xToolkit import xfile
from hctest_excel_to.excel_to import Excel

test_list=xfile.read("G:\zidonghua\接口测试用例.xls").excel_to_dict(sheet=1)
print(test_list)

{
    'application':'web',
    'application_client_type':'pc'
}

{
 "accounts": "huace_001",
 "pwd": "huace_001",
}