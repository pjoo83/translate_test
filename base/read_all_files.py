import os


def find_file(search_path, include_str=None, filter_strs=None):
    if filter_strs is None:
        filter_strs = []

    files = []
    # 获取路径下所有文件
    names = os.listdir(search_path)
    for name in names:
        path = os.path.abspath(os.path.join(search_path, name))
        if os.path.isfile(path):
            # 如果不包含指定字符串则
            if include_str is not None and include_str not in name:
                continue

            # 如果未break，说明不包含filter_strs中的字符
            for filter_str in filter_strs:
                if filter_str in name:
                    break
            else:
                files.append(path)
        else:
            files += find_file(path, include_str=include_str, filter_strs=filter_strs)
    return files


# 读取多有文件夹
def find_dos():
    a = os.listdir("docs/Songs")
    for i in a:
        if i.endswith(".meta"):
            a.remove(i)
    return a


# if __name__ == '__main__':
#     # 获取全部文件
#     # f = find_file("./txt")
#     # print(f)
#
#     # # 获取包含指定字符的文件
#     f = find_file("../data/test_data", include_str="en")
#     #
#     # # 获取不包含指定字符的文件
#     # f = find_file(r"data", filter_strs=["en", ".txt", ".ogg", "__init__"])
#     # print(f)
#     #
#     # # 获取包含指定字符且不包含某些指定字符的文件
#     # f = find_file(r"docs/Songs", include_str=" ", filter_strs=[".meta", "__init__"])
#     # print(f)
