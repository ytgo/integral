#原神微信积分商城
import requests
import yaml

# 读取配置文件
with open('config.yml', 'r') as f:
    config = yaml.safe_load(f)

headers = {
    "Host": "hk4e-api.mihoyo.com",
    "Connection": "keep-alive",
    "xweb_xhr": "1",
    "x-rpc-token": config['x_rpc_token'],
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/11237",
    "Content-Type": "application/json",
    "Accept": "*/*",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://servicewechat.com/wx3b919a574b90c5de/4/page-frame.html",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9"
}

response = requests.post("https://hk4e-api.mihoyo.com/event/weixinpointsmall/sign", headers=headers)

if response.status_code == 200:
    json_data = response.json()
    if 'message' in json_data:
        print(json_data['message'])
else:
    print(f"Request failed with status code {response.status_code}")
