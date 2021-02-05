import json
import os
from readConfig import proDir

jsonPath = os.path.join(proDir, 'testFIle')


class OperationJson:
    # 操作json文件
    def __init__(self, file_path=None):
        if file_path==None:
            # self.file_path = os.path.join(proDir, 'testFile', file_path)
            self.file_path = jsonPath+"/data"
        else:
            self.file_path = self.read_data()
        self.data = self.read_data()

    def read_data(self):
        """
        读取json文件
        :return:
        """
        with open(jsonPath+"/data", 'rb') as fp:
            data = json.load(fp)
            return data



    def get_data(self, id):
        """
        根据关键字获取对应数据
        :return:
        """
        return self.data[id]

    def write_data(self, data):
        with open(jsonPath+"/token", 'w') as fp:
            json.dump(data, fp)
            print("加载成功")
            #fp.write(json.dump(data))


if __name__ == '__main__':
    file_path = jsonPath+"/data"
    opejson = OperationJson()
    print(opejson.read_data())
    print(opejson.get_data("user"))
    """
    data = {
        "username": "Jane_cm_qj",
        "password": "abc@123456"
    }
    #print(type(data))
    opejson.write_data(data)
    
    """



