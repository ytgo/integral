import httpx
import yaml
import os

# 获取脚本所在的目录
script_dir = os.path.dirname(os.path.abspath(__file__))
# 构建 config.yml 文件的绝对路径
config_path = os.path.join(script_dir, '..', 'config.yml')

try:
    with open(config_path, 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)
except FileNotFoundError:
    print(f"错误：未找到 {config_path} 文件。")
    raise
except yaml.YAMLError as e:
    print(f"错误：解析 {config_path} 文件时出错 - {e}")
    raise

# 设置请求头
headers = {
    "Host": "superapp-public.kiwa-tech.com",
    "sec-ch-ua-platform": "Android",
    "_haidilao_app_token": config["_haidilao_app_token"],
    "sec-ch-ua": "Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Android WebView\";v=\"134\"",
    "sec-ch-ua-mobile": "?1",
    "reqtype": "APPH5",
    "deviceid": "null",
    "user-agent": "Mozilla/5.0 (Linux; Android 14; M2012K11AC Build/UKQ1.230804.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/134.0.6998.136 Mobile Safari/537.36 XWEB/1340043 MMWEBSDK/20241103 MMWEBID/1977 MicroMessenger/8.0.55.2780(0x2800373D) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 miniProgram/wx1ddeb67115f30d1a",
    "accept": "application/json, text/plain, */*",
    "content-type": "application/json",
    "origin": "https://superapp-public.kiwa-tech.com",
    "x-requested-with": "com.tencent.mm",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": f"https://superapp-public.kiwa-tech.com/app-sign-in/?SignInToken={config['_haidilao_app_token']}&source=MiniApp",
    "accept-encoding": "gzip, deflate, br, zstd",
    "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "cookie": config["cookie"]
}

# 请求体（JSON 数据）
data = {
    "signinSource": "MiniApp"
}

# 目标 URL
url = "https://superapp-public.kiwa-tech.com/activity/wxapp/signin/signin"

try:
    # 创建支持 HTTP/2 的客户端
    with httpx.Client(http2=True) as client:
        # 发送 POST 请求
        response = client.post(url, headers=headers, json=data)
        response_json = response.json()
        if response_json["success"] is False:
            print(response_json["msg"])
        else:
            for item in response_json["data"]["signinQueryDetailList"]:
                print(item["fragment"])
except httpx.RequestError as e:
    print("请求出错:", e)
