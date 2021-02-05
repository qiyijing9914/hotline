import json
import requests
from readConfig import ReadConfig
from util.oper_json import OperationJson
from util.common_util import CommonUtil

requests.packages.urllib3.disable_warnings()
baseurl = ReadConfig().get_http("baseurl")


class RunMethod:
    def post_main(self, url, data, header=None):
        response = None
        if header != None:
            response = requests.post(url=url, data=data, headers=header, verify=False)
        else:
            response = requests.post(url=url, data=data, verify=False)
        return response.json()

    def get_main(self, url, data=None, header=None):
        response = None
        if header != None:
            response = requests.get(url=url, params=data, headers=header, verify=False)
        else:
            response = requests.get(url=url, params=data, verify=False)
        return response.json()

    def patch_main(self, url, data = None, header = None):
        response = None
        if header != None:
            response = requests.patch(url=url, data=data, headers=header, verify=False)
        else:
            response = requests.patch(url=url, data=data, verify=False)
        return response.json()

    def put_main(self,url, data = None, header = None):
        response:None
        if header != None:
            response = requests.put(url=url, data=data, headers=header, verify=False)
        else:
            response = requests.put(url=url, data=data, verify=False)
        return response.json()

    def run_main(self, method, url, data=None, header=None):
        res = None
        if method == 'post':
            res = self.post_main(url, data, header)
        elif method == 'patch':
            res = self.patch_main(url, data, header)
        elif method == 'put':
            res = self.put_main(url, data, header)
        else:
            res = self.get_main(url, data, header)
        return json.dumps(res, indent=2, sort_keys=True, ensure_ascii=False)


if __name__ == '__main__':
    if __name__ == '__main__':
        """
              url = baseurl + 'app/users/login'
              # print(url)
              #data = {"username": "Jane_cm_qj", "password": "abc@123456"}
              data=OperationJson().get_data('user')
              #print(type(data))
              header = {'Content-Type': 'application/json;charset=utf-8'}
              json_data = json.dumps(data)
              # print(type(json_data))
              run = RunMethod().run_main(method="post", url=url, data=json_data, header=header)
              token = json.loads(run)['data']
              print(token)
          """

        url = " http://172.16.25.62/api/web/events/20201106000261?" \
             "token=d5323a12a84dac0a42784aa33090a04d&id=20201106000261&currentStatus=1"
        data = {"status": "12", "desc": "同意受理！", "withNext": 0, "params": ""}
        json_data = json.dumps(data)
        print(type(json_data))
        header = {'Content-Type': 'application/json;charset=utf-8'}
        run = RunMethod().run_main(method="patch", url=url, data=json_data, header=header)
        print(run)




