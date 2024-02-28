import pymysql


def execute_sql(channel_id, newly_quantity, modify_quantity, quantity):
    db = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='zxcv1234',
        database='localhost_interface'
    )
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

if __name__ == '__main__':
    execute_sql(2, 30, 50, 900)
