import json
class CommonUtil:
    def is_contain(self, str_one, str_two):
        # 判断一个字符串是否存在另一个字符串
        flag = None
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag


if __name__ == "__main__":
    a = CommonUtil()
    x = {"name": "qyj", "age": "18"}
    #x=json.dumps(x)
    y = "name"
    #y=json.dumps(y)
    b = a.is_contain(y,x)
    print(b)
