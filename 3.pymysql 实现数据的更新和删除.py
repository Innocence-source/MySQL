"""
1. 事务:commit() 和 rollback()

MySQL InnoDB:
        - 执行 delete /insert/update 后，数据只是在事务缓冲区，没有真正落盘
        - conn.commit():提交事务，永久保存修改
        - conn.rollback():回滚，放弃本次所有修改，恢复到执行前状态
    场景:删除过程中报错，就执行 rollback, 防止删一半。
"""
# 导入 pymysql 库, pymysql操作mysql的第三方包
import pymysql


# 先把连接对象初始化为 None, 后面用来判断是否成功连上数据库
conn = None


try:
    # 建立 MySQL 数据库连接
    # 用户名、密码、 服务器地址、 端口号、要操作的数据库名
    conn = pymysql.connect(user='root', password='', host='localhost', port=3306, database='py2607b')

    # conn.cursor() 来创建游标 cursor，游标就是 SQL 执行器，用来发送 SQL 给数据库、拿到结果
    # 上下文管理器写法。with 代码块结束后，自动关闭 cursor，不用手动写 cursor.close ()，
    # 省去 开始cursor = conn.cursor()、结尾cursor.close()
    with conn.cursor() as cursor:

        # 定义删除SQL语句，%s 是pymysql的占位符，不是python字符串格式化！
        # 绝对不要用字符串拼接id，防止SQL注入
        sql = """
            delete from tb_qiku where id = %s
        """

        # 执行sql，args=(id,) 把id变量传给占位符%s
        # args必须是元组，(id,)逗号不能少，否则不是元组
        rows = cursor.execute(sql, args=(id, ))

        print(f"删除成功、影响 {rows}行")

        # 提交事务！mysql默认InnoDB引擎是事务型，DML(增删改)必须commit才真正写入数据库
        conn.commit()

# 捕获所有异常（裸except，不推荐生产使用）
except:

    # 如果连接已经创建成功，发生异常就回滚事务，撤销本次修改
    if conn is not None:
        conn.rollback()

    # raise:抛出捕获到的异常，不让异常被吞掉，外部能看到报错信息
    raise

# finally 无论try正常执行、还是触发异常，一定会执行
finally:
    if conn is not None:

        # 如果数据库连接存在，关闭连接，释放数据库资源
        conn.close()