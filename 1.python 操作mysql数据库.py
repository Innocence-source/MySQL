import pymysql 


conn = None 

try:
    # 创建和数据库的连接对象 
    conn = pymysql.connect(user="root", password="", host="localhost", port=3306, database="py2607b")
    # 创建一个 SQL 执行器 对象 
    # cursor = conn.cursor() 
    with conn.cursor() as cursor:
        # 编写一个 SQL命令  
        sql = """
            create table tb_qiku(
                id bigint primary key auto_increment, 
                name varchar(10) comment '公司名',
                address varchar(100) comment '公司地址'
            )
        """
        # 使用 执行器 执行 SQL命令 、并 获取 命令影响的行数
        rows = cursor.execute(sql)
        # 输出影响的行数 
        print(rows)
    # 关闭 SQL 执行器、释放资源 
    # cursor.close()
finally:
    # 管理 SQL 链接 
    if conn is not None: 
        conn.close()



