#!/usr/bin/python
#-*-coding:utf-8-*-






# def zhishu():
#     sum=0
# a=int(input('输入开始值'))
# b=int(input('输入结束值'))
# if a>=2:
#     for i in range(a,b+1):
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             sum+=i
#     print('您的质数之和是%d'%sum)
# else:
#     print(

# a=[12,23,45,78,56,41,1]
# #b=a.sort()
# c=a.reverse()
# print(a)

# goods=[['西瓜',200],['黄瓜',110],['南瓜',320],['傻瓜',420],['哈达瓜',150]]
# yimai=[]
# qian=int(input('你有多少钱'))
# if not qian.isdigit():
#     exit()

# class Lei():   #class 类名：(类名首字母要大写)
#     pass
# Lei()               #调用方式   类名（）
#
#
# class Man():                  #类名
#     def eat(self):            #属性
#         print('----吃----')
#     def drink(self):
#         print('-----喝----')
#     def sleep(self):
#         print('----睡-----')
#     def prinfo(self):
#         print(self.color)
#         print(self.leg)
# beautiful_tall_huang=Man()           #对象
# beautiful_tall_huang.eat()           #方法（行为）
# beautiful_tall_huang.drink()
# beautiful_tall_huang.sleep()
# #beautiful_tall_huang.play()
# beautiful_tall_huang.color='花色'
# #print(beautiful_tall_huang.color)
# # beautiful_tall_huang.weiba='有'
# # print(beautiful_tall_huang.weiba)
# beautiful_tall_huang.leg='四条'
# # print(beautiful_tall_huang.leg)
# beautiful_tall_huang.prinfo()
# beautiful_tall_huang=Man()
# beautiful_tall_huang.color='黑'
# beautiful_tall_huang.leg='四'
# beautiful_tall_huang.prinfo()

# class Cat():
#     #jjj='nihao'
#     #属性
#     def __init__(self,newweiba,newcolor):
#         self.weiba=newweiba
#         self.color=newcolor
#         #self.leg=newleg
#     def __str__(self):
#         msg='有没有尾巴'+self.weiba+'\n颜色是:'+self.color
#         return msg
#     #方法
#     def __eat(self):
#          print('----吃----')
#          return 1
#     def drink(self):
#          print('----喝----')
# xiaohuamao=Cat('有','花色')
# print(xiaohuamao)
# xiaobaimao=Cat('没有','白色')
# print(xiaobaimao)

    #def sleep(self):
        #print('---睡----')
    #def wc(self):
#         #print('---啦---')
#     def prinfo(self):
#         print(self.__color)
#         print(self.weiba)
#         print(self.__leg)
# big_baimao=Cat('有','花色','四')
# # big_baimao.eat()
# # big_baimao.drink()
# #big_baimao.wc()
# # big_baimao.color='花色'
# # big_baimao.weiba='有'
# #big_baimao.leg='四'
# big_baimao.prinfo()

#烤地瓜
#class Sweetpotato:
#定义属性，一般用来完成一些初始化的工作
'''
    def __init__(self):
        self.cookedleve1=0
        self.cookedstring='生的'
        self.condiments=[]
    def __str__(self):
        msg='地瓜的生熟程度:'+self.cookedstring
        msg+='\n地瓜的等级为:'+str(self.cookedleve1)
        msg+='\n添加佐料为:'
        if len(self.condiments)>0:
            for i in self.condiments:
                msg+=i+','
            msg=msg.strip(',')
            #msg = msg[:-1]
        else:
            msg+='当前没有添加佐料'
        return msg
    def cook(self,times):
        self.cookedleve1+=times
        if self.cookedleve1>8:
            self.cookedstring='烤成木炭了'
        elif self.cookedleve1>5:
            self.cookedstring='已经烤好了'
        elif self.cookedleve1>3:
            self.cookedstring='半生不熟'
        else:
            self.cookedstring='生的'
    def addcondiments(self,temp):
        self.condiments.append(temp)
digua=Sweetpotato()
print(digua)
digua.cook(4)
digua.addcondiments('芥末')
print(digua)
digua.cook(3)
digua.addcondiments('盐')
print(digua)
digua.cook(3)
print(digua)
'''

