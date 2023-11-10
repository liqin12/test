import  requests
import jsonpath

params={
    'application':'app',
    'application_client_type':'weixin',
}

data={
    'accounts':'huace_xm',
    'pwd':123456,
    'type':'username'
}
url='http://shop-xo.hctestedu.com/index.php?s=/api/user/login'
res=requests.post(url=url,params=params,data=data)
print(res.text)
token=res.json()['data']['token']

token_list=jsonpath.jsonpath(res.json(),'$..token')

"""
    如何处理接口关联！
        使用jsonpath结合变量传递token数据信息
"""
# 接口测试   需要登录信息 token
carturl='http://shop-xo.hctestedu.com/index.php?s=/api/cart/save&token={}'.format(token_list[0])
data2={
    'goods_id':'2',
    'spec':[
        {
            'type':'套餐',
            'value':'套餐二'
        },
        {
            'type':'颜色',
            'value':'银色'
        },
        {
            'type':'容量',
            'value':'64G'
        },
    ],
    'stock':2
}
res2=requests.post(url=carturl,params=params,data=data2)

print(res2.text)

data3={
    'id':12
}
requests.post(url='http://shop-xo.hctestedu.com/index.php?s=/api/goods/favor&token={}'.format(token_list[0]),
              params=params,data=data3)
"""
    加密接口如何测试
"""