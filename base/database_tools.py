import pymysql
import datetime


def execute_sql(channel_id, newly_quantity, modify_quantity, quantity, method):
    db = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='zxcv1234',
        database='localhost_interface'
    )
    if method == 'insert':
        insert_execute_statistics = "insert into translate_statistics (channel_id,newly_quantity,modify_quantity,quantity) " \
                                    "values (%s,%s,%s,%s)"
        values = channel_id, newly_quantity, modify_quantity, quantity
        cursor = db.cursor()
        try:
            cursor.execute(insert_execute_statistics, values)
            db.commit()
            print('插入成功数据库成功')
        except pymysql.MySQLError as e:
            print(e, '插入失败')

        data1 = cursor.fetchone()
        data2 = cursor.fetchall()
        db.close()
    elif method == 'query':
        select_execute_statistics =f"SELECT a.time from translate_statistics a INNER JOIN translate_channel " \
                                   f"b on a.channel_id =b.channel_id where b.channel ='ios' ORDER BY time desc;   "
        cursor = db.cursor()
        try:
            cursor.execute(select_execute_statistics)
            result = cursor.fetchone()
            print('查询结果', result)
            dt = result[0]
            next_day_midnight = (dt + datetime.timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
            timestamp_ms = int(next_day_midnight.timestamp() * 1000)
            return timestamp_ms
        except pymysql.MySQLError as e:
            print(e, '查询错误')


if __name__ == '__main__':
    execute_sql(2, 30, 50, 900, 'query')
