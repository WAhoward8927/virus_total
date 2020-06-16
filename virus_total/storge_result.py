"""存檔功能，如遇特殊檔名會另外做處理"""
import os
import re
from virus_total import grep_dict


def create(path_name_type, input_target, result):
    """建立資料夾與指定檔名，接收參數：資料夾名稱、目前掃描資料、掃描結果"""
    result_dir = f'.\\{path_name_type}_result'
    try:
        os.mkdir(result_dir)
    except FileExistsError:
        pass
    if path_name_type == "Url":  # 掃描到URL類型時,檔案命名須特別處理
        replace1 = input_target.replace("\n", "")
        replace2 = re.sub('[\/*|:"<>?\\\\]', '∮', replace1)
        special_file_path = f"{result_dir}\\{replace2}_ScanResult.txt"  # 先替換所有特殊字元
        if len(special_file_path) > 260:  # 路徑+檔名過長處理
            trim_file_name = to_long(special_file_path)
            grep_dict.grep_data(result, trim_file_name, input_target)
        else:
            grep_dict.grep_data(result, special_file_path, input_target)
    else:
        replace_special_char = re.sub('[\/*|:"<>?\\\\]', '', input_target)
        file_path = f"{result_dir}\\{replace_special_char}_ScanResult.txt"
        grep_dict.grep_data(result, file_path)


def to_long(target):
    rm_extension = os.path.splitext(target)[0]  # 移除附檔名
    rm_base_char = rm_extension.split('_ScanResult')[0]  # 移除_ScanResult
    keep_extension = os.path.splitext(target)[1]  # 保留副檔名
    total_len = 200 - (len(rm_base_char) + 15)  # 路徑+檔名+副檔名必須在260字元內
    capture_file_name = rm_base_char[:total_len]
    special_file_path = f"{capture_file_name}_ScanResult{keep_extension}"
    return special_file_path
