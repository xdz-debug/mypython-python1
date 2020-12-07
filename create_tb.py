'''
定义一个创建表的的函数，从tb_sql中传入表名和建表sql，通过判断库中是否有该表名，无则建表。
'''


import pymysql
import hashlib

def lanjie():
    conn = pymysql.connect(host="127.0.0.1",user ="root", password ="111111",database ="test",charset ="utf8mb4")
    cursor = conn.cursor()

def insert_tb(v1,v2,va1,sql2):#用户注册
    conn = pymysql.connect(host="127.0.0.1",user ="root", password ="111111",database ="test",charset ="utf8mb4")
    cursor = conn.cursor()
    sql1 ="select count(*) from %s where user_name='%s' "%(v1,va1)
    try:
        cursor.execute(sql1)# 执行sql语句
        result = cursor.fetchone()
        aa=int(result[0])
        if aa==0:
            try:
                cursor.execute(sql2)
                print(sql2)
                print("保存成功")
                conn.commit()
            except:
                print("保存%s失败"%v2)

        else:
            print("该用户%s已注册"%v2)

    except:
        conn.rollback()# 发生错误时回滚
        print("操作失败")
    conn.close()
     
def select_tb(v1,v2,sql2):#用户登录验证
    conn = pymysql.connect(host="127.0.0.1",user ="root", password ="111111",database ="test",charset ="utf8mb4")
    cursor = conn.cursor()
    sql1 ="select count(*) from information_schema.TABLES t where t.TABLE_SCHEMA ='test' and t.TABLE_NAME ='%s'"%v1
    try:
        cursor.execute(sql1)# 执行sql语句
        result = cursor.fetchone()
        aa=int(result[0])
        if aa==1:
            try:
                cursor.execute(sql2)
                res= cursor.fetchone()
                id= int(res[0])
                print("%s登录成功"%v2)
                conn.commit()
                return id
            except:
                print("%s用户名或密码错误，登录失败"%v2)

        elif aa==1:
            print("没有该用户")
        conn.close()
    except:
        conn.rollback()# 发生错误时回滚
        print("操作失败")
        conn.close()


def update_tb(id,sux):#更新属性
    conn = pymysql.connect(host="127.0.0.1",user ="root", password ="111111",database ="test",charset ="utf8mb4")
    cursor = conn.cursor()
    sql1="select * from tb_suxing where id=%d"%id
    try:
        cursor.execute(sql1)# 执行sql语句
        result = cursor.fetchone()
        a1=int(result[1])
        a2=int(result[2])
        a3=int(result[3])
        a4=int(result[4])
        a5=int(result[5])
        a6=int(result[6])
        a7=int(result[7])
        a8=int(result[8])
        try:
            gj=sux[0]+a1
            fy=sux[1]+a2
            sm=sux[2]+a3
            shan=sux[3]+a4
            mz=sux[4]+a5
            ren=sux[5]+a6
            bjl=sux[6]+a7
            dj=sux[6]+a8
            sql2="update tb_suxing set gj=%d,fy=%d,sm=%d,shan=%d,mz=%d,ren=%d,bjl=%d,dj=%d where id =%d"%(gj,\
            fy,sm,shan,mz,ren,bjl,dj,id)
            cursor.execute(sql2)
            conn.commit()
            return 1
        except:
            print("保存出错")
            conn.rollback()# 发生错误时回滚
            return 0
        
    except:
        sql11="insert into tb_suxing set id =%d"%id
        cursor.execute(sql11)
        conn.commit()
        return 0
    conn.close()

def select_tb_sux(id):#查询属性
    conn = pymysql.connect(host="127.0.0.1",user ="root", password ="111111",database ="test",charset ="utf8mb4")
    cursor = conn.cursor()
    sql1="select * from tb_suxing where id=%d"%id
    try:
        cursor.execute(sql1)# 执行sql语句
        result = cursor.fetchone()
        a1=int(result[1])
        a2=int(result[2])
        a3=int(result[3])
        a4=int(result[4])
        a5=int(result[5])
        a6=int(result[6])
        a7=int(result[7])
        a8=int(result[8])
        sux=[a1,a2,a3,a4,a5,a6,a7,a8]
        return sux
        
    except:
        return 0
    conn.close()
def select_tb_user(id):#查询用户名
    conn = pymysql.connect(host="127.0.0.1",user ="root", password ="111111",database ="test",charset ="utf8mb4")
    cursor = conn.cursor()
    sql1="select user_name from tb_user where id=%d"%id
    try:
        cursor.execute(sql1)# 执行sql语句
        result = cursor.fetchone()
        p=result[0]
        return p   
    except:
        return 0
    conn.close()