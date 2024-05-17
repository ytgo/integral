import requests
import json


# cookie
member_id = "XXXXX"
token = "XXXXX"
deviceId = "XXXX"
UA = "Mozilla/5.0 (Linux; Android 10; MI 6 Build/10; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.104 Mobile Safari/537.36/TcTravel/10.8.4"

# 定义请求的URL
url1 = "https://tcmobileapi.17usoft.com/platformsign/sign/signIndex"
url2 = "https://tcmobileapi.17usoft.com/platformsign/task/commit"
url3 = "https://tcmobileapi.17usoft.com/platformsign/task/receive"

# 定义请求的头部
headers = {
    "Host": "tcmobileapi.17usoft.com",
    "Connection": "keep-alive",
    "Content-Length": "400",
    "Accept": "application/json, text/plain, */*",
    "User-Agent": UA,
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "https://appnew.ly.com",
    "X-Requested-With": "com.tongcheng.android",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://appnew.ly.com/",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
}


data1 = {
	"isReceive": 1,
    "memberId": member_id,
	"platId": 100,
	"reqFrom": "app",
	"regid": "",
	"deviceId": deviceId,
	"token": token,
  }

# 任务ID列表
task_ids = [231, 232, 194, 186]

# 遍历每个任务ID
for task_id in task_ids:
    # 定义请求的数据
    data2 = {
        "taskId": task_id,
        "memberId": member_id,
        "reqFrom": "app",
        "platId": 100
    }

    data3 = {
        "taskId": task_id,
        "memberId": member_id,
        "reqFrom": "app",
        "token": token,
        "platId": 100,
        "deviceId": deviceId,
    }

    #发送签到请求
    response1 = requests.post(url1, headers=headers, json=data1)
    json_data = response1.text
    # 解析JSON数据
    parsed_data = json.loads(json_data)

    # 输出里程余额和签到信息
    mileage_balance = parsed_data['data']['mileageBalance']
    sign_info = parsed_data['data']['signInfo']

    print(f"里程余额: {mileage_balance}")

    #发送任务请求
    response2 = requests.post(url2, headers=headers, json=data2)
    print(response2.text)

    # 发送领取里程请求
    response3 = requests.post(url3, headers=headers, json=data3)
    print(response3.text)
