
import requests
import json
import datetime



#利用青龙调用alist批量修改文件夹内的文件名称

#自行替换
username = "用户名"
password = "密码"
device_address = "http://xxx.xxx.com"
# =================== 下方为方法，文件底部为请求方法自行替换文件目录 ==================

#  调用登录 获取token
url = device_address+"/api/auth/login"

# 组装登录信息
payload = json.dumps({
    "username": username,
    "password": password
})
headers = {
    'Content-Type': 'application/json'
}
# 调用接口
response = requests.request("POST", url, headers=headers, data=payload).json()
# 获取token
token = response.get("data").get('token')
# 输出日志
print(datetime.datetime.now(), "当前token为：", token)


# 正则表达式修改文件名称
def send(token, src_dir):
    url = device_address + "/api/fs/regex_rename"
    # 正则表达式规则
    payload = json.dumps({

        "src_dir": src_dir,  # 需改的目录
        "src_name_regex": ".epub.epub", # 源名称
        "new_name_regex": ".epub" # 需要改的名称
    })
    headers = {

        'Authorization': token,  # 登录信息
        'Content-Type': 'application/json'
    }
    # 调用接
    response = requests.request("POST", url, headers=headers, data=payload)
    print(datetime.datetime.now(), " 本次修改", src_dir, "目录下文件名称返回信息：", response.text)

# 需要修改的目录，反正是自己 写的有啥参数需要加就在这添加就好
send(token, "/kodo");
send(token, "/GBooks");


