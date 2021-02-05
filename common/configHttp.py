# _*_ coding:utf-8
"""
import requests
import readConfig as readConfig
from common.testLog import MyLog as Log
import json
import Common

localReadConfig = readConfig.ReadConfig()


class ConfigHttp:
    def __init__(self):
        global host, port, timeout
        host = localReadConfig.get_http("baseurl")
        port = localReadConfig.get_http("port")
        timeout = localReadConfig.get_http("timeout")
        self.log = Log.get_log()
        self.logger = self.log.logger
        self.headers = {}
        self.params = {}
        self.data = {}
        self.url = None
        self.files = {}

    def set_url(self, url):
        self.url = host + url

    def set_headers(self, header):
        self.headers = header

    def set_params(self, param):
        self.params = param

    def set_data(self, data):
        self.data = data

    def set_files(self, file):
        self.files = file

    # defined http get method
    def get(self):
        try:
            response = requests.get(self.url, params=self.params, headers=self.headers, timeout=float(timeout))
            # response.raise_for_status()
            return response.json()
        except TimeoutError:
            self.logger.error('Time out!')
            return None

    # defined http post method
    def post(self):
        try:
            # response = requests.post(self.url, data=self.data, headers=self.headers, timeout=float(timeout))
            response = requests.post(self.url, self.data, self.headers, float(timeout))
            return response.json()
        except TimeoutError:
            self.logger.error('Time out!')
            return None

     def run_main(self, method, url, data=None, header=None):
        res = None
        if method == 'Post':
            res = self.post_main(url, data, header)
        else:
            res = self.get_main(url, data, header)
        return json.dumps(res, indent=2, sort_keys=True, ensure_ascii=False)




def login():
    url = 'http://172.16.25.62/api/app/users/login'
    header = {'Content-Type': 'application/json;charset=utf-8'}
    data = {"username": "Jane_cm_qj", "password": "abc@123456"}
    json_data = json.dumps(data)
    # print(json_data)
    # print(type(json_data))
    timeout = 10
    res = ConfigHttp.post(url, headers=header, data=json_data, timeout=timeout)
    auth_token = res.json()['data']['token']
    return auth_token


if __name__ == '__main__':
    url = 'http://172.16.25.62/api/app/users/login'
    header = {'Content-Type': 'application/json;charset=utf-8'}
    user = Common.get_xls('testcase.xlsx', 'test1')
    # print(user)
    data = {"username": user[1][0], "password": user[1][1]}
    json_data = json.dumps(data)
    timeout = 10
    res = requests.post(url=url, headers=header, data=json_data, timeout=timeout)
    print("响应状态码：", res.status_code)
    print("响应消息：", res.text)
    print("请求头：", res.request.headers)
    print("响应头：", res.headers)
    print("响应数据：", res.text)
    print("cookie：", res.cookies)

#print("json：", res.json())
"""


