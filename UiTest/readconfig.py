# 读取配置信息
import configparser
import os
proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir, "config.ini")

class ReadConfig:
    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.cf.read(configPath)

    def get_http(self, param):
        value = self.cf.get("http", param)
        return value

    def get_db(self, param):
        value = self.cf.get("database", param)
        return value

if __name__ == '__main__':
    test = ReadConfig()
    # LocalIp = test.get_http('baseurl')
    LocalIp = test.get_db('ip')
    print(LocalIp)