import pymysql
conn = pymysql.connect(host="127.0.0.1",user ="root", password ="111111",database ="test",charset ="utf8mb4")
cursor = conn.cursor()

def a():
    sql='select * from tb_user'
    cursor.execute(sql)# 执行sql语句
    result = cursor.fetchone()
    aa=int(result[0])
    print(aa)

    
def b():
    sql='select * from tb_user'
    cursor.execute(sql)# 执行sql语句
    result = cursor.fetchone()
    aa=int(result[2])
    print(aa)

a()
b()