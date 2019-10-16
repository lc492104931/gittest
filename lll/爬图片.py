#!/usr/bin/python
#-*-coding:utf-8-*-

# import re
# #import json
# import requests
# a='http://www.quanshuwang.com/book/7/7549/2429683.html'
# b=requests.get(a)
# print(b)
# c=b.content.decode('gbk')
# print(c)
#
# guolv=re.compile('id="content".*?<div class="attention">',re.S)
# answer=guolv.findall(c)
# print(answer)
# list=re.findall(r'')
# print(list)

# with open('梨视频.png','wb') as s:
#     s.write(c)

#爬虫第一步：分析网址的变化
#第二步：分析网页源代码，通过正则表达式过度
#第三步：根据过滤出来的内容，保存
#://movie.douban.com/top250'


# import requests
# import re
# class Douban(object):
#     def qingqiu(self):
#         url='https://movie.douban.com/top250'
#         head='User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0{}'
#         res=requests.get(url=url,headers=head)
#         h=res.content.decode('utf8')
#         return h


# a=int(input('>>'))
# if a%2==0 or a%3==0:
#     print('hello world')
#     if a %2==0:
#         print('hello')
#     elif a%3==0:
#             print('word')
# else:
#     print(123)

#i love this game  写成 game this love i

# a='i love this game'
# b=a.split( )
# print(b)
# b.reverse()
# print(b)
# s=' '.join(b)
# print(s)



#将其中最大和第二最大写出来，包括两个99
# a=[1,2,3,4,4,5]
#
# for i in range():
#     if i>:
#         print(i)

# a = []
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if i != j and i != k and j != k:
#                 b = i*100+j*10+k
#                 if b not in a:
#                     a.append(b)
# print(a)

#因数之和
# a=int(input('输入数字'))
# b=[]
# for i in range(1,a):
#     if a%i==0:
#         b.append(i)
# d=sum(b)
# if d==a:
#     print(a)
# else:
#     print('不相等')



#公鸡母鸡小鸡
# for i in range(0,50):
#     for j in range(0,101):
#         for k in range(0,101):
#             if i+j+k==100 and 2*i+1*j+0.5*k==100:
#                 a = '公鸡：{}，母鸡：{}，小鸡：{}'.format(i,j,k)
#                 print(a)

#冒泡排序
# def paixu(*args):
#     a=list(args)
#     for i in range(len(a)):
#         for j in range(i+1,len(a)):
#             if a[i]>a[j]:
#                 a[i],a[j]=a[j],a[i]
#     print(a)
# paixu(12,23,21,45)


#列表中的元素往左移一位
# a=[1,23,12,31]
# for i in range(len(a)-3):##左移
#     a.insert(len(a),a[0])
#     a.remove(a[0])
#     print(a)

# a=[x for x in range(10) if x > 7]
# print(a)

# a=open(r'C:\Users\lll\Desktop\006faQNTgw1f5wnm06h3ug30ci08cake.gif','rb')
# b=a.read()
# print(b)
# q=open('s.gif','wb')
# q.write(b)

# import xlwt
# with open('11.txt','w',encoding='ansi') as a :
#     a.write('11111\n'*20)
# xl=xlwt.Workbook(encoding='utf8')
# sheet=xl.add_sheet('123')
#
# with open('11.txt','r',encoding='utf8')as q:
#     b=q.readlines()
#     for i ,j in enumerate(b):
#         w=j.split(',')
#         for m ,n in enumerate(w):
#             sheet.write(i,m,n)
# xl.save('a.xls')


# import re
# #import json
# import requests
# a='http://www.quanshuwang.com/book/7/7549/2429683.html'
# b=requests.get(a)
# c=b.content.decode('gbk')
# #print(c)
#
# guolv=re.compile('</script>&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<script type="text/javascript">style6',re.S)
# answer=guolv.findall(c)
# #print(answer)
# for i in answer:
#      b=i.replace('<br />\r\n<br','\n')
#      d=b.replace('/>\r\n&nbsp;&nbsp;&nbsp;&nbsp;','\n')
#      f=d.replace('()',' ')
#      print(f)
# with open('狼图腾.txt','w',encoding='utf8') as a:
#     a.write(f)

#爬虫第一步：分析网址的变化
#第二步：分析网页源代码，通过正则表达式过度
#第三步：根据过滤出来的内容，保存
#://movie.douban.com/top250'

#面对对象爬小说
'''
import requests
import re
class Lang(object):
    def __init__(self,url,bianma,lv):
        self.url=url
        self.binama=bianma
        self.lv=lv

    def qingqiu(self):
        #url='http://www.quanshuwang.com/book/7/7549/2429683.html'
        head='User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'
        res=requests.get(self.url,head)
        h=res.content.decode(self.binama)
        return h
    def guo(self):
        guolv = re.compile(self.lv, re.S)   下面括号里的就是self.lv
        #guolv = re.compile('</script>&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<script type="text/javascript">style6', re.S)
        answer=guolv.findall(self.qingqiu())
        #print(answer)
        for i in answer:
             b=i.replace('<br />\r\n<br','')
             d=b.replace('/>\r\n&nbsp;&nbsp;&nbsp;&nbsp;','\n')
             f=d.replace('()',' ')
             return f
    def txt(self):
        with open('狼图腾1.txt','w',encoding='utf8') as a:
            a.write(self.guo())
a=Lang('http://www.quanshuwang.com/book/7/7549/2429683.html','gbk',
    '</script>&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<script type="text/javascript">style6')

a.txt()
from time import sleep
sleep(2)
'''

'''
import xlwt
import xlrd
# with open('1.txt','w',encoding='utf8')as a:
#     a.write('aa,ss,dd,ff'*5)
#将数据导入到excel
xl=xlwt.Workbook(encoding='utf8')
sheet=xl.add_sheet('haha')
with open('1.txt','r',encoding='utf8') as b:
    c=b.readlines()
    #print(c)
    for i,j in enumerate(c):
        #print(j)
        h=j.split(',')
        print(h)
        for m,n in enumerate(h):
            print(h)
            # for i,j in enumerate(f):
            sheet.write(i,m,n)

        #for j,k in enumerate(i):
            #sheet.write(n,j,i)
xl.save('a.xls')
'''

import xlwt
a=xlwt.Workbook(encoding='utf8')
sheet=a.add_sheet('haha')
for i in range(10):
    for j in range(10):
        sheet.write(i,j)
a.save()












