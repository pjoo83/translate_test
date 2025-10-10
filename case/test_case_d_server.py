from base.check_tools import start_check
from base.read_all_files import find_file
from base.check_tools import absolute_path
import pandas as pd
from base.ef_download import ef_download


def test_check():
    """
         服务端内容检查
    """
    files = find_file("/Users/lbj/Desktop/starx/project/translate_test/data/server_key")
    server_files = files[0]
    df_excel = pd.read_excel(server_files)
    first_column_excel = df_excel.iloc[:, 0].to_list()
    ef_download('server', first_column_excel)
    start_check("server")
    # if len(files) > 1:
    #     start_check("server")
    # else:
    #     print("server_data文件中只有一个多语言文件，需要再下一份，保持文件夹中有两文件，就可以开始")
