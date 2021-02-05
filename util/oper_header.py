import json
from readConfig import ReadConfig
from util.oper_json import OperationJson
#import Common
import requests
from common.runmethond  import RunMethod

baseurl = ReadConfig().get_http("baseurl")


class OperationHeader:

    def __init__(self, response):
        self.response = json.loads(response)

    def get_response_token(self):
        """
        获取登录返回的token
        :return:
        """
        token = {"data": {"token": self.response['data']['token']}}
        return token

    def write_token(self):
        op_json = OperationJson()
        op_json.write_data(self.get_response_token())


if __name__ == '__main__':
    url = baseurl + 'app/users/login'
    # print(url)
    data = {"username": "Jane_cmjd", "password": "abc@123456"}
    header = {'Content-Type': 'application/json;charset=utf-8'}
    json_data = json.dumps(data)
    res = RunMethod().run_main(method="post", url=url, data=json_data, header=header)
    print(res)
    op = OperationHeader(res).get_response_token()
    print(op)
    #op.write_token()


