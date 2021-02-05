import os
import codecs
import configparser

proDir = os.path.split(os.path.realpath(__file__))[0]
# print(proDir)
configPath = os.path.join(proDir, 'config')
# print(configPath)
"""fd = open(configPath)
data = fd.read()
print(data)"""


class ReadConfig:
    def __init__(self):
        fd = open(configPath)
        data = fd.read()

        # remove BOM
        if data[:3] == codecs.BOM_UTF8:
            data = data[3:]
            file = codecs.open(configPath, "w")
            file.write(data)
            file.close()
        fd.close()

        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_http(self, name):
        value = self.cf.get("HTTP", name)
        return value

    def get_db(self, name):
        value = self.cf.get("DATABASE", name)
        return value

    def get_params(self,name):
        value = self.cf.get("PARAMS",name)
        return value


if __name__ == "__main__":
    x = ReadConfig()
    s = x.get_http("baseurl")
    print(s)




