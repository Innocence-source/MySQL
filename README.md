# Python 操作 MySQL 数据库

配置 虚拟环境 

CTRL + SHIFT + P --->  > Python Select Interpreter

需要 安装依赖库  pymysql  

```
pip install pymysql
```

使用步骤 

1. 导入 依赖库

```
import pymysql
```

1. 创建数据库连接对象

```
conn = pymysql.connect(user='root',  password='', host='localhost', port=3306, database='xxxx')
```

1. 获取 SQL 执行器

```
cursor = conn.cursor()
```

1. 定义 SQL 命令

```
sql = """
    insert into tb_user(username, password, tel, gender, create_time) values(%s, %s, %s, %s, now())
"""
```

** SQL命令中 表示数据的地方需要使用 占位符代替、 %s 或者 %(name)s  **

1. 执行 SQL 命令、并获取结果

```
rows = cursor.execute(sql, args=...)
```

** %s 占位符 传入 元组对象、  %(name)s 传入 字典对象 ** 

- DML 命令 必须在事务环境下 进行 提交 或者 回滚操作 
- insert 命令 可以 使用 `cursor.lastrowid` 获取插入的(自动增长)主键
- 查询 命令 需要通过 `cursor.fetchone`,  `cursor.fetchall`, `cursor.fetchmany` 等方法 获取结果集

1. 关闭资源

```
cursor.close()

conn.close()
```

