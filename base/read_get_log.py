import logging
import time

# 创建logger对象
logger = logging.getLogger('check_language')

# 设置日志等级
# 创建时间单位
# localtime = time.localtime(time.time())
time = time.strftime('%Y年%m月%d日 %H点-%M分-%S秒', time.localtime(time.time()))

print(time, "开始测试！！！！！！！！！")
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=f'../logs/{time}test.log',
                    filemode='w', encoding='utf-8')
# test_log = logging.FileHandler(filename=f'{time}test.log', mode='w', encoding='utf-8')

# 向文件输出的日志级别
# test_log.setLevel(logging.DEBUG)

# 向文件输出的日志信息格式
# formatter = logging.Formatter('%(asctime)s - %(filename)s  - %(message)s')
# '%(asctime)s - %(filename)s - line:%(lineno)d - %(levelname)s - %(message)s'

# 给处理器设置格式
# test_log.setFormatter(formatter)

# 加载文件到logger对象中
# logger.addHandler(test_log)
