import pandas as pd
import glob
import os
import time
import shutil


def merge_files(channel):
    # 语言文件所在的目录
    language_folder = "base/language/"
    # 目标合并文件
    output_file = file_name(channel)

    # 获取所有 .xlsx 文件并排序
    xlsx_files = sorted(glob.glob(os.path.join(language_folder, "*.xlsx")))

    # 确保 `en.xlsx` 是第一个文件
    en_file = None
    for file in xlsx_files:
        if "en" in os.path.basename(file).lower():  # 识别 en 文件
            en_file = file
            break

    if not en_file:
        print("未找到 en.xlsx 文件，请检查")
        exit()

    # 读取 `en.xlsx` 作为基准文件
    base_df = pd.read_excel(en_file, dtype=str)

    # 获取 `Key` 列（默认第一列）
    key_col = base_df.columns[0]

    # 确保 `en` 语言列的名称正确
    en_column_name = "en"
    if base_df.columns[1] != en_column_name:
        base_df.rename(columns={base_df.columns[1]: en_column_name}, inplace=True)

    # 移除 `en.xlsx` 让后续文件不重复处理
    xlsx_files.remove(en_file)

    # 遍历其他语言文件
    for file in xlsx_files:
        df = pd.read_excel(file, dtype=str)

        # 提取语言名称（文件名去除 `.xlsx`）
        lang_name = os.path.basename(file).replace(".xlsx", "")

        # 读取第一列（Key）和第二列（对应语言翻译）
        file_key_col = df.columns[0]
        file_value_col = df.columns[1]

        # 创建 Key -> Value 映射
        key_value_map = dict(zip(df[file_key_col], df[file_value_col]))

        # 按 `Key` 匹配数据，无法匹配的留空
        base_df[lang_name] = base_df[key_col].map(key_value_map)

    # 如果 `comment` 列存在，移动到最后一列
    if "comment" in base_df.columns:
        comment_col = base_df.pop("comment")
        base_df["comment"] = comment_col

    # 保存最终合并的 Excel 文件
    base_df.to_excel(output_file, index=False, sheet_name="Merged Data")

    print(f"合并完成，文件已保存到 {output_file}")


def absolute_path(data):
    """
    :return: 获取绝对路径
    """
    folder_name = f'{data}'
    folder_path = os.path.abspath(folder_name)
    return folder_path


def file_name(channel):
    times = time.strftime('%Y年%m月%d日 %H点-%M分', time.localtime(time.time()))
    # if channel == 'server':
    #     new_name = fr"{absolute_path('data')}/{channel}_data/{times}language_{channel}.csv"
    #     return new_name
    # else:
    new_name = fr"{absolute_path('data')}/{channel}_data/{times}language_{channel}.xlsx"
    return new_name


def clear_folder(folder_path):
    if not os.path.exists(folder_path):
        print(f"文件夹 '{folder_path}' 不存在！")
        return

    # 删除文件夹内所有内容
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)  # 删除文件或符号链接
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)  # 删除整个文件夹
        except Exception as e:
            print(f"删除 '{file_path}' 失败: {e}")

    print(f"文件夹 '{folder_path}' 已清空！")
