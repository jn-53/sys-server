# encoding:utf-8
# 根据您选择的AK已为您生成调用代码
# 检测到您当前的AK设置了IP白名单校验
# 您的IP白名单中的IP非公网IP，请设置为公网IP，否则将请求失败
# 请在IP地址为0.0.0.0/0 外网IP的计算发起请求，否则将请求失败
import json

import requests
import os

os.environ["HTTP_PROXY"] = ""
os.environ["HTTPS_PROXY"] = ""
os.environ["NO_PROXY"] = "*"

# 服务地址
host = "https://api.map.baidu.com"

# 接口地址
uri = "/weather/v1/"

# 此处填写你在控制台-应用管理-创建应用后获取的AK
ak = "ICbCuMnbV9i8A3AoH0r0HiB7zw9YiIOp"

params = {
    "district_id": "222405",
    "data_type": "all",
    "ak": ak,

}

response = requests.get(url=host + uri, params=params)
if response:
    print(json.dumps(response.json(), ensure_ascii=False, indent=None))

