import time
import string
from base.read_all_files import find_file
from base.trans_reading import read_file, rows
from deepdiff import DeepDiff
import re
import shutil
import os
import openpyxl
from openpyxl.styles import PatternFill
from openpyxl.comments import Comment


def start_check(channel):
    global language1, language2
    files = find_file(f"D:/project/translate/data/{channel}_data", include_str="language",
                      filter_strs=["~"])
    fil = files[:-3:-1]
    language1 = read_file(fil[0])
    language2 = read_file(fil[1])
    check_tools(channel)


# 检测
def check_tools(channel):
    """
    :param channel: 选择对应端
    :return: 返回差异内容
    """
    max1 = rows(language1)
    max2 = rows(language2)
    if max1 == max2:
        # logger.info(F"本次行数相同,共计key{max1 - 1}条")
        datas_key = different_key()
        if len(datas_key) > 0:
            # logger.info(f"本次修改了key，{datas_key}")
            datas = different_data(language1)
            msg = [f"本次修改了key，{datas_key}"]
            msg2 = []
            data = ""
            generate_xlsx(file=language1, file_list=datas, msg=msg, channel=channel, msg2=msg2, datas=data)
        else:
            # logger.info("本次内容未新增key,下面进行内容检查")
            dif_msg = different_msg()
            if len(dif_msg[0]) > 0:
                msg = [f"本次检测共有{len(dif_msg[0])}条的值出现变化,修改后的详情见下方！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！"]
                msg2 = []
                data = ""
                generate_xlsx(file=language1, file_list=dif_msg[0], msg=msg, channel=channel, msg2=msg2, datas=data)
            else:
                # logger.info(f"本次未修改KEY，也未对值进行修改")
                print(f"本次未修改KEY，也未对值进行修改")
    elif max1 < max2:
        rol = different_row_number()
        rol = [i + 2 for i in rol]
        msg = [f"本次多语言在{rol}行减少,共减少{max2 - max1}条"]
        # datas_key = different_key()
        datas = different_data(language2)
        # logger.info(f"第{rol}行减少key有{datas_key}")
        msg2 = []
        data = ""
        generate_xlsx(file=language2, file_list=datas, msg=msg, channel=channel, msg2=msg2, datas=data)
    elif max1 > max2:
        # datas_key = different_key()
        rol = different_row_number()
        rol = [i + 2 for i in rol]
        msg = [f"本次多语言在{rol}行新增,共新增{max1 - max2}条"]
        datas1 = different_data(language1)
        datas2 = add_change_diff(language1)
        datas = [datas1, datas2[0]]
        # logger.info(f"第{rol}增加key{datas_key}")
        if len(datas2[0]) > 0:
            msg2 = [f"本次检测共有{len(datas2[0])}条多语言的值出现变化,修改后的详情见下方！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！"]
        else:
            msg2 = [f"本次只有新增，没有修改多语言"]
        generate_xlsx(file=language1, file_list=datas, msg=msg, channel=channel, msg2=msg2, datas=datas2)


def different_key():
    """
    :return: 获取差异key 与行数
    """
    old_file = language2.iloc[:, 0].tolist()
    new_file = language1.iloc[:, 0].tolist()
    diff = DeepDiff(old_file, new_file)
    return diff


def different_msg():
    """
    :return: 没有新增时，对比所有差异数据
    """
    diff_msg = []
    diff = []
    old_file = language2.values.tolist()
    new_file = language1.values.tolist()
    for i in range(len(new_file) - 1, -1, -1):
        if new_file[i] != old_file[i]:
            diff_msg.append(new_file[i])
            a = DeepDiff(old_file[i], new_file[i])
            diff.append(a)
    return diff_msg, diff


# 既有变化也有修改
def add_change_diff(language):
    """
    :param language: 传入语言列表
    :return: 返回变化内容与变化
    """
    diff_msg = []
    diff = []
    diff_num = different_row_number()
    diff_data = different_data(language)
    old_file = language2.values.tolist()
    new_file = language.values.tolist()
    for data in range(len(diff_num)):
        old_file.insert(diff_num[data], diff_data[data])
    for i in range(len(new_file) - 1, -1, -1):
        if new_file[i] != old_file[i]:
            diff_msg.append(new_file[i])
            a = DeepDiff(old_file[i], new_file[i])
            diff.append(a)
    return diff_msg, diff


def different_row_number():
    """
    :return: 返回差异行
    """
    key_rol = []
    dif_keys = different_key().keys()
    for key in dif_keys:
        dif_values = different_key()[key]
        for keys in dif_values:
            numbers_list = re.findall(r'\d+', keys)
            numbers = "".join(numbers_list)
            key_rol.append(int(numbers))
    return key_rol


def different_data(file_name):
    """
    :param file_name: 传入文件名
    :return:  获取每行差异数据
    """
    data_list = []
    dif_num = different_row_number()
    for data_num in dif_num:
        data_list.append(file_name.loc[data_num].to_list())
    return data_list


def generate_xlsx(file, file_list, msg, msg2, channel, datas):
    """
    :param file:文件名
    :param file_list:
    :param msg: 写入新增值
    :param msg2:写入变换值
    :param channel:创建文件名的端名
    :param datas:变化的内容
    :return: 写入表格文件
    """
    times = time.strftime('%Y年%m月%d日 %H点-%M分-%S秒', time.localtime(time.time()))
    new_name = f"D:/project/translate/result/{times}--{channel}--language_test.xlsx"
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.append(msg)
    head = get_head(file)
    sheet.append(head)
    for file in file_list:
        for i in file:
            print(i)
            sheet.append(i)
        if msg2:
            sheet.append(msg2)
            msg2 = False
    insert_edit_cols(sheet)
    if datas != "":
        get_line_value(datas[1], sheet)
    workbook.save(new_name)


def get_head(file):
    """
    :param file: 传入下载文件
    :return: 返回文件表头
    """
    head = file.keys().tolist()
    return head


def change_filename(client):
    """
    :param client: 传入对应端名称
    :return: 文件名修改，并移动到指定文件夹
    """
    Dpath = os.path.expanduser(r'~\Downloads')
    # print(Dpath)
    import time
    times = time.strftime('%Y年%m月%d日 %H点-%M分-%S秒', time.localtime(time.time()))
    new_name = f"D:/project/translate/data/{client}_data/{times}language_{client}.xlsx"
    en_file = find_file(Dpath, include_str='en', filter_strs=[".~"])
    shutil.move(en_file[0], new_name)
    print(f'{new_name}文件移动成功')


# 文件移动
# def move_file(client):
#     change_filename(client)
#     data_path = f"D:/project/translate/data/{client}_data"
#     en_file = find_file(f'C:/Users/123123/Downloads', include_str=f'language_{client}', filter_strs=[".~"])
#     shutil.move(en_file[0], data_path)
#     sleep(3)


#
def insert_edit_cols(sheet):
    """
    :param sheet: 传入文件名
    :return: 插入编辑列
    """
    sheet.insert_cols(idx=1, amount=2)
    sheet["A2"] = "完成备注"
    sheet['B2'] = "编号"


def get_line_value(values, sheet):
    """
    :param values: 传入变化的内容变化内容
    :param sheet: 传入文件表
    :return: 向表格插入变化值
    """
    max1 = rows(language1)
    max2 = rows(language2)
    line = max1 - max2 + 4
    for i in range(len(values)):
        for k, v in values[i].items():
            for k1, v1 in v.items():
                line1 = letters_to_num(k1) + 3
                color_fill(sheet, line, line1)
                comment = Comment(str(v1), "hhhh")
                letters = number_to_letter(line1)
                str_num = str(line)
                nl = letters + str_num
                sheet[nl].comment = comment
        line += 1


# 转化数字
def letters_to_num(letter):
    """
    :param letter: 表格字母
    :return:返回对应的数字
    """
    result = ""
    for char in letter:
        if char.isdigit():
            result += char
    return int(result)


def number_to_letter(number):
    """
    :param number: 传入对应行的数
    :return: 数字转化为字母
    """
    if 1 <= number <= 26:
        return string.ascii_uppercase[number - 1]
    elif number > 26:
        return "A" + string.ascii_uppercase[number - 26 - 1]


def color_fill(sheet, row, column):
    """
    :param sheet: 传入的对应表格地址
    :param row: 对应的行
    :param column:
    :return:
    """
    fill = PatternFill('solid', fgColor='f8c600')
    sheet.cell(row, column).fill = fill
