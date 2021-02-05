import urllib

from common.runmethond import RunMethod
import json
from readConfig import ReadConfig
from util.oper_json import OperationJson
from util.oper_header import OperationHeader
from util.mydb import myDB
import pytest
import readConfig

baseurl = ReadConfig().get_http("baseurl")
localcode = ReadConfig().get_params("code")
sql="select event_id from event where code=%s"
a = myDB().executeSQL(sql=sql,params=localcode)
event_id=myDB().get_one(a)
global pub_data
pub_data={}




def test_login():
    url = baseurl + 'app/users/login'
    # print(url)
    data = OperationJson().get_data("user")
    header = {'Content-Type': 'application/json;charset=utf-8'}
    json_data = json.dumps(data)
    # print(type(json_data))
    res = RunMethod().run_main(method="post", url=url, data=json_data, header=header)
    pub_token= OperationHeader(res).get_response_token()
    pub_data['token'] = pub_token['data']['token']
    pub_data['id'] = str(event_id[0])
    print(pub_data)
    #OperationHeader(res).write_token()
    # op = OperationHeader(res)
    # op.write_token()
    #print(res)
    assert json.loads(res)['code']==200

def test_discover():
    #pub_data['currentStatus'] = 1
    url = baseurl +"web/events/" +event_id[0]+'?' + \
          urllib.parse.urlencode(pub_data)+'&'+'currentStatus=1'
    print(url)
    data={"data":{"status":"12","desc":"同意受理！","withNext":0,"params":""}}
    json_data=json.dumps(data)
    res = RunMethod().run_main(method='patch',url=url,data=json_data)
    assert json.loads(res)['code'] == 200

def test_case():
    url = baseurl + "web/events/" + event_id[0] + '?' + \
          urllib.parse.urlencode(pub_data) + '&' + 'currentStatus=2'
    data ={"mode":1,"data":{"status":"13","desc":"同意立案！","withNext":0,"params":""}}
    json_data = json.dumps(data)
    res = RunMethod().run_main(method='put', url=url, data=json_data)
    assert json.loads(res)['code'] == 200

