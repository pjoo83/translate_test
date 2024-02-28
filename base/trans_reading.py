import xlrd
import pandas as pds


# 文件读取
def read_path(path):
    file_path = path
    data = xlrd.open_workbook(file_path)
    table = data.sheet_by_name('en_ar_bn_cs_de_es_fr_in_it_ja_k')
    return table


# 文件读取pandas
def read_file(path):
    file = pds.read_excel(path)
    # file = files.sort_values(by='key_name', inplace=True)
    return file


# 获取最大行数
def rows(path):
    max_rows, max_cols = path.shape
    return max_rows

#
# # 文件读取pandas
# def read_file1(path):
#     file = pd.read_csv(path, encoding='ISO-8859-1')
#     return file
#
#
# # print(read_file1(r"C:\Users\123123\Desktop\tranlate\data\test_data\en (1).csv"))
#
#
# def csv_to_xlsx_pd():
#     csv = pd.read_csv(r'C:\Users\123123\Desktop\tranlate\data\test_data\en (1).csv', encoding='ISO-8859-1')
#     csv.to_excel(r'C:\Users\123123\Desktop\tranlate\data\test_data\en (1).xlsx', sheet_name='data')
#
#
# if __name__ == '__main__':
#     # csv_to_xlsx_pd()
