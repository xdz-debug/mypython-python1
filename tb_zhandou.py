'''
战斗模式
'''
import create_tb
#import dl
import random

def gjcz():
    
    brave=create_tb.select_tb_sux(5)
    monster=create_tb.select_tb_sux(1001)
    print(brave,monster)



'''
攻击模式
命中率=自身命中/（自身命中+敌方闪避）
暴击率=自身暴击/（自身暴击+敌方韧性）
伤害=攻击力*攻击力/（攻击力+敌方防御力）*（）
'''
def zdms(p1,p2,u1,u2):#p1攻击p2
        a1=int(u1[0])
        a2=int(u1[1])
        a3=int(u1[2])
        a4=int(u1[3])
        a5=int(u1[4])
        a6=int(u1[5])
        a7=int(u1[6])
        a8=int(u1[7])
        b1=int(u2[0])
        b2=int(u2[1])
        b3=int(u2[2])
        b4=int(u2[3])
        b5=int(u2[4])
        b6=int(u2[5])
        b7=int(u2[6])
        b8=int(u2[7])
        sb=random.randint(0,a5+b4)
        if sb>=a5:
            print("%s闪避了%s的攻击"%(p2,p1))
            sh=0
        else:
            bj=random.randint(0,a7+b6)
            if bj<=a7:
                sh=a1*a1/(a1+b2)*2
                print("%s的攻击产生了暴击，对%s造成%d的伤害"%(p1,p2,sh))
            
            else:
                sh=a1*a1/(a1+b2)
                print("%s的攻击对%s造成%d的伤害"%(p1,p2,sh))
        b3 = b3-sh
        if b3<=0:
            print("%s击败了%s"%(p1,p2))
            b3=0

        u1=[a1,a2,a3,a4,a5,a6,a7,a8]
        u2=[b1,b2,b3,b4,b5,b6,b7,b8]
        return u1,u2

