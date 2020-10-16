"""判斷檔名與格式"""
import os
import glob


def file_check():
    """四種檔案類型的內容排列必需一列一筆"""
    target_file_name = ['domaindata', 'urldata', 'ipdata', 'filedata']
    check_list = list()  # 過濾完的結果
    for search in target_file_name:
        result = glob.glob(f'{os.getcwd()}/{search}.*')  # 抓出此檔案的絕對路徑，加上特定檔名
        file_extension = ['txt', 'csv', 'xls', 'xlsx']  # 特定副檔名
        for file_name in result:  # 迭代找到指定檔名的檔案
            for extension_name in file_extension:  # 濾出特定副檔名
                if file_name.endswith(extension_name):
                    check_list.append(file_name)
    return check_list
