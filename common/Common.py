import os
from data import data_config
from readConfig import proDir
from testLog import MyLog as Log

# localConfigHttp = configHttp.ConfigHttp()
log = Log.get_log()
logger = log.logger

"""
def get_xls(xls_name, sheet_name):
    cls = []
    # 获取xls文件路径
    xlsPath = os.path.join(proDir, 'testFile', xls_name)
    file = data_config.open_excel(xlsPath)
    sheet = data_config.get_sheet(sheet_name)
    nrows = data_config.get_rows(sheet)
    # cols = excel.get_cols(sheet)
    # param = excel.get_content(sheet, nrows)
    for i in range(1, nrows):
        if sheet.row_values(i)[0] != u'case_name':
            cls.append(sheet.row_values(i))
    return cls


if __name__ == '__main__':
    case = get_xls('testcase.xlsx', 'test1')
    print(case[0][1])
"""


def get_xls(xls_name):

    # 获取xls文件路径
    xlsPath = os.path.join(proDir, 'testFile', xls_name)
    file = data_config.open_excel(xlsPath)
   # sheet = data_config.get_sheet(sheet_name)
    #nrows = data_config.get_rows(sheet)
    # cols = excel.get_cols(sheet)
    # param = excel.get_content(sheet, nrows)


if __name__ == '__main__':
    case = get_xls('testcase.xlsx')
    print(case)
# 从xml文件中读取sql语句