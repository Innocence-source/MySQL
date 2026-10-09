"""
1. DML 命令 必须 在 事务环境下 才能工作 、否则 增、删、改 都不会影响表中的数据。

    解决 无法插入问题 :

        a) 在创建连接对象的时候 设置 autocommit=True(自动提交)、 不推荐、这种做法每一个 SQL 命令都是一个单独的事务环境
        违背了事务概念 。

        b) 手动 提交 或者 回滚 事务 。

            业务成功 提交事务 、 业务失败 回滚事务

    pymysql 默认关闭自动提交, 执行 insert / update / delete (DML 增删改) 只是写在临时事务缓存里, 不写commit(), 数据库里不会真正保存数据。

2. 区分 DDL 和 DML(考试重点)
    1. DML(增删改 insert/update/delete)：受事务控制, 需要 commit
    2. DDL(建表、删表 create/drop/alter)：执行的时候自动提交事务, 不需要手动 commit

3.举例子理解事务:
    比如同时做 2 条插入：
        - 两条都成功 → commit, 两条数据入库
        - 第 1 条成功, 第 2 条报错 → rollback, 第一条也撤销, 数据库一条都不新增, 不会出现只插入一半的脏数据。

"""


import pymysql


# 创建一个数据库连接对象
conn = None
try:
    conn = pymysql.connect(user="root", password="", host="localhost", port=3306, database="py2607b")

    # 定义要执行的 SQL 命令
    # 在 SQL 命令中, 如果 需要 数据、必须使用 占位符 代替 、防止产生 SQL 注入的风险
    #    数据通常来自 网页、网页中的数据是由 用户输入的, 为了解决 SQL 注入(工具)、服务器 在 定义SQL 时候, 数据必须用占位符
    #
    #    %s        : 如果 使用 该格式的占位符 、那么 传入数据时候 需要通过 元组的 方式 传入 数据
    #    %(name)s  : 如果 使用 该格式的占位符、那么 传入数据时候 需要通过 字典的 方式 传入 数据
    #

    sql = """
        insert into tb_qiku(name, address) values (%(name)s, %(address)s)
    """

    # 创建一个 SQL 执行器
    with conn.cursor() as cursor:

        params = {"name": "奇酷网络科技有限公司", "address": "郑州市金水区东三街"}
        # 执行 SQL, 并传入 数据
        rows = cursor.execute(sql, args=params)
        # 输出 结果、lastrowid 用来获取 插入成功的 主键 (主键必须是自动增长)
        print(f"插入成功、影响行数为 {rows}, 当前数据的主键: { cursor.lastrowid }")

    # 业务成功、提交事务
    conn.commit()

except:
    # 如果产生异常、业务失败
    conn.rollback()
    # 抛出错误
    raise

finally:
    if conn is not None:
        conn.close()
