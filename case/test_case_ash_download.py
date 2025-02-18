import subprocess
from base.sh_download import clear_folder
from base.sh_download import merge_files


def test_run_ios_download():
    clear_folder('base/language')
    process = subprocess.run(['sh', '/Users/lbj/Desktop/starx/project/translate_test/base/main.sh', 'ios'],
                             capture_output=True, text=True)
    # 检查脚本的输出
    print(f"Error output: {process.stderr}")
    print(f"Standard output: {process.stdout}")
    assert process.returncode == 0  # 确保脚本执行成功
    merge_files('ios')
    # assert "Hello from test script!" in process.stdout  # 检查输出内容


def test_run_android_download():
    clear_folder('base/language')
    process = subprocess.run(['sh', '/Users/lbj/Desktop/starx/project/translate_test/base/main.sh', 'android'],
                             capture_output=True, text=True)
    # 检查脚本的输出
    print(f"Error output: {process.stderr}")
    print(f"Standard output: {process.stdout}")
    assert process.returncode == 0  # 确保脚本执行成功
    merge_files('android')


def test_run_cocos_download():
    clear_folder('base/language')
    process = subprocess.run(['sh', '/Users/lbj/Desktop/starx/project/translate_test/base/main.sh', 'cocos'],
                             capture_output=True, text=True)
    # 检查脚本的输出
    print(f"Error output: {process.stderr}")
    print(f"Standard output: {process.stdout}")
    assert process.returncode == 0  # 确保脚本执行成功
    merge_files('cocos')


def test_run_server_download():
    clear_folder('base/language')
    process = subprocess.run(['sh', '/Users/lbj/Desktop/starx/project/translate_test/base/main.sh', 'server'],
                             capture_output=True, text=True)
    # 检查脚本的输出
    print(f"Error output: {process.stderr}")
    print(f"Standard output: {process.stdout}")
    assert process.returncode == 0  # 确保脚本执行成功
    merge_files('server')