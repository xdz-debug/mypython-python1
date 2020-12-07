'''
商城

'''
import random
def choujiang():
    input("请选择，装备商城a，金币商城b：")
    a=random.randint(1,100)

    print(a)



#装备商城
def zbsc():
    pass

#金币商城
def jbsc(jb):
    jb-=300
    a=random.randint(1,6)
    print("您摇到了%d点，获得%d点金币"%(a,a*100))
    jb+=a*100
    print("剩余金币%d"%jb)

jbsc(300)

