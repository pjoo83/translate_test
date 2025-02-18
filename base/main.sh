##!/bin/bash
PROJECT_DIR=$(dirname $(readlink -f "$0"))
cd $PROJECT_DIR || exit 1

echo "当前工作路径：$PROJECT_DIR"
#
#cmd=$1
#if [ "$cmd" == "android" ]; then
#    phrase pull --config phrase_pull_config_csv.yml
#    # 总会下载一个en-.json的文件，删除
#    rm -f "./language/en-.xlsx"
#fi
#    #python3 language_file_tools.py download
#if [ "$cmd" == "ios" ]; then
#  phrase pull --config phrase_pull_config_csv.yml
#fi
#if [ "$cmd" == "cocos" ]; then
#  phrase pull --config phrase_pull_config_csv.yml
#fi
#if [ "$cmd" == "server" ]; then
#  phrase pull --config phrase_pull_config_csv.yml
#fi
#
#read -p "Press Enter to continue..."
#!/bin/bash

#!/bin/bash

# 获取命令行传入的参数
cmd=$1

# 设置默认的 access_token 和 project_id
access_token=""
project_id=""

# 根据 cmd 参数选择不同的配置


if [ "$cmd" == "ios" ]; then
    access_token="403f7b41bbe055f7f19ed7e58f93f8f04a22d271066b5a7abf283f7690343f5a"
    project_id="1a374225727009b986e6362f02b8cd4f"
fi

if [ "$cmd" == "android" ]; then
    access_token="07be57ad97bc0a5c6972672d0347b8206ae7802b4f7b2e15ccf3bbd270ef86c8"
    project_id="b568a11c6a1cd2b9a358645f139caa81"
fi

if [ "$cmd" == "cocos" ]; then
    access_token="60de135389b35128b4d172c1143c66a206b20b626b06e96793454ae30d10aedc"
    project_id="c988bd901906b54229aab53f016d6b76"
fi

if [ "$cmd" == "server" ]; then
    access_token="fca3b0e9454cab334b5e5f02f7da1b327499a9d5beb212556ca83ce89cd23a43"
    project_id="0ab5e482e6ca2b925b50b1998d7d8deb"
fi

# 检查是否有正确的 cmd 参数
if [ -z "$access_token" ] || [ -z "$project_id" ]; then
    echo "Invalid command: Please specify a valid option (android, ios, cocos, server)"
    exit 1
fi

# 打印读取的配置（仅调试时使用）
echo "Access Token: $access_token"
echo "Project ID: $project_id"

# 导出环境变量
export ACCESS_TOKEN=$access_token
export PROJECT_ID=$project_id

# 使用 envsubst 替换 yml 配置文件中的变量
config_file_path="./phrase_pull_config_csv.yml"
temp_config_file="./phrase_pull_config_temp.yml"

if [ ! -f "$config_file_path" ]; then
    echo "Configuration file $config_file_path does not exist!"
    exit 1
fi

envsubst < "$config_file_path" > "$temp_config_file"

# 确保临时配置文件已生成
if [ ! -f "$temp_config_file" ]; then
    echo "Failed to generate temp config file"
    exit 1
fi

# 如果 cmd 为 ios，删除 tags 字段
if [ "$cmd" == "ios" ]; then
    sed -i '' '/tags:/d' "$temp_config_file"
fi

if [ "$cmd" == "server" ]; then
    sed -i '' '/tags:/d' "$temp_config_file"
fi
if [ "$cmd" == "android" ]; then
    sed -i '' '/tags:/d' "$temp_config_file"
fi
# 执行 phrase pull 命令，使用临时替换后的配置文件
phrase pull --config "$temp_config_file"

# 删除临时生成的配置文件（如果不再需要）
rm "$temp_config_file"