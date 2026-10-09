import pymysql 


conn = None 

try:
    # 创建数据库连接对象 
    conn = pymysql.connect(user="root", password="", database="py2607b")

    # 定义要执行的 SQL 命令 
    sql = """
        select name as company_name, address, id from tb_qiku 
    """
    # 创建 SQL 执行器 
    with conn.cursor() as cursor:
        # 执行 SQL 
        rows = cursor.execute(sql)
        # 输出结果 
        print(f"查询成功、返回的数据个数: {rows}")
        # 获取 查询的结果 
        #  fetchone :  一次提取满足条件的一条数据 、返回一个元组 
        #  fetchall :  一次性提取满足条件的所有数据 、返回一个 二维元组 
        #  fetchmany : 支持传入一个 数字、代表一次性提取 多少条数据

        data = cursor.fetchall()
        print(f"查询到的数据是: {data}")

        # 获取 查询的 列 、返回一个 二维元组、 元组中的每一个值 代表一个 列、 且 值的 第一个数据 代表 列名
        columns = [column[0] for column in cursor.description] 

        print(f"查询的列有: {columns}")

        # 将 查询的列 和 数据 进行合并 、形成 字典 
        data = [dict(zip(columns, d)) for d in data]

        print(f"合并后的数据: {data}")

finally:
    if conn: 
        conn.close()