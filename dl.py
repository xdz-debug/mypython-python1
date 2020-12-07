'''
账号登录、账号注册
'''
import create_tb
import hashlib
import tb_zhandou

def charu_user():
    v1='tb_user'
    v2='用户表'
    va1=input("请输入用户名:")
    va2=input("请输入密码:")
    va3=input("请输入邮箱:")
    va4=input("请输入姓名:")
    va5=input("请输入联系电话:")
    va6=input("请输入个人描述:")
    m = hashlib.md5()
    b = va2.encode(encoding='utf-8')
    m.update(b)
    str_md5 = m.hexdigest()
    
    sql2 = "insert into tb_user(user_name,mima,mail,name,phone,miaoshu)\
         values('%s','%s','%s','%s','%s','%s')"%(va1,str_md5,va3,va4,va5,va6)
    create_tb.insert_tb(v1,v2,va1,sql2)



def sle_user():
    v1='tb_user'
    va1=input("请输入用户名:")
    va2=input("请输入密码:")
    m = hashlib.md5()
    b = va2.encode(encoding='utf-8')
    m.update(b)
    str_md5 = m.hexdigest()
    sql2 = "select * from tb_user where user_name='%s' and mima='%s'"%(va1,str_md5)
    id =create_tb.select_tb(v1,va1,sql2)
    return id

def up_suxing(id):

    sux=[1,0,0,0,0,0,0]
    a=create_tb.update_tb(id,sux)
    return a

#玩家对战
def wjdz():
    p1=create_tb.select_tb_user(5)
    p2=create_tb.select_tb_user(7)
    u1=create_tb.select_tb_sux(5)
    u2=create_tb.select_tb_sux(7)
    print(u1,u2)
    while 1:
        u2,u1=tb_zhandou.zdms(p1,p2,u1,u2)
        if u1[2]==0 or u2[2]==0:
            break
        else:
            p1,p2=p2,p1


def gwdz():
    p1=create_tb.select_tb_user(5)
    p2=create_tb.select_tb_user(7)
    u1=create_tb.select_tb_sux(5)
    u2=create_tb.select_tb_sux(7)
    print(u1,u2)
    while 1:
        u2,u1=tb_zhandou.zdms(p1,p2,u1,u2)
        if u1[2]==0 or u2[2]==0:
            break
        else:
            p1,p2=p2,p1


sle_user()