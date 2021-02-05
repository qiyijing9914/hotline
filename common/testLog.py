import logging
from datetime import datetime
import threading
import readConfig
import os


class TestLog:
    def __init__(self):
        global logPath, resultPath, proDir
        proDir = readConfig.proDir
        resultPath = os.path.join(proDir, "result")
        # 如果 result file不存在，则创建result file
        if not os.path.exists(resultPath):
            os.mkdir(resultPath)
        # defined test result file name by localtime
        logPath = os.path.join(resultPath, str(datetime.now().strftime("%Y%m%d%H%S")))
        # creat log file if it doesn't exist
        if not os.path.exists(logPath):
            os.mkdir(logPath)
        # defined logger
        self.logger = logging.getLogger()
        # defined log level
        self.logger.setLevel(logging.INFO)
        # defined handler 用于写入日志文件
        handler = logging.FileHandler(os.path.join(logPath, "output.log"))
        # defined formatter ，定义handler输出格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        # add handler
        self.logger.addHandler(handler)


class MyLog:
    log = None
    mutex = threading.Lock()

    def __init__(self):
        pass

    @staticmethod
    def get_log():
        if MyLog.log is None:
            MyLog.mutex.acquire()
            MyLog.log = TestLog()
            MyLog.mutex.release()
        return MyLog.log
