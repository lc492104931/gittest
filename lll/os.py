#!/usr/bin/python
#-*-coding:utf-8-*-
#os  实现python与操作系统之间的交互
import os

#popen()   执行cmd命令
# aa=os.popen('ping 192.168.2.127')
# print(aa.read())

#getcwd  获取当前所在目录
#print(os.getcwd())

#chdir  切换目录
# os.chdir('c:')
# print(os.getcwd())

#mkdir  创建目录
#os.mkdir('haha')

#创建递归目录
#os.makedirs('qqq/www/eee')

#删除递归目录
#os.removedirs('qqq/www/eee')

#删除空目录
#os.rmdir('haha')

#删除文件
#os.remove('')

#文件重命名 ,前面是老文件名，后面新文件名
#os.rename('.py','.py')

#获取目录下的所有文件  listdir
#print(os.listdir('f:'))#括号里写哪个路径就可以看哪个路径下的所有文件

#将文件与路径分隔开
# a=os.path.split(r'‪C:\Users\lll\Desktop\hei')
# print(a)

#将文件后缀名与路径分隔开 ,不管是错误路径还是正确路径都会分隔显示的，只是为了显示
# a=os.path.splitext(r'F:\untitled\lll\heihei.py')
# print(a)

#判断文件是否是目录  TRUE是的  False不是
# a=os.path.isdir(r'lll')
# print(a)

#统计当前目录下有多少个目录文件，有多少普通文件
# a=[]
# b=os.listdir(r'f:')
# #print(b)
# for a in b:
#     print(a)
#
# c=a.endswith('.py')
# print(c)



#paramiko  封装了ssh协议，主要用于远程控制
#import paramiko
#
# #创建一个ssh的客户端
# ssh11=paramiko.SSHClient()
# #将第一次连接的主机跳过验证，添加到know_host文件中
# ssh11.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh11.connect(hostname='192.168.2.119',port=22,username='root',password='123456')
# a,b,c=ssh11.exec_command('ls -al')  #括号里的命令要输入直接出来结果的。a，b，c可以用这三个代替：
#                          # stuin 指输入的命令   stuout 指命令运行后的结果  stuerr 指命令的报错
# ss=b.read().decode('utf8') #括号里的编码方式不加也可以，.decode()
# print(ss)
# #断开连接
# ssh11.close()

'''
#使用paramiko中的sftpclient组件传输文件
#1 建立一个传输通道，填入ip地址和端口号（是一个元组）
import paramiko
transport=paramiko.Transport(('192.168.2.119',22))
#2 连接主机，只需输入用户名和密码
transport.connect(username='root',password='123456')
#3 创建一个sftp客户端
sftp_client=paramiko.SFTPClient.from_transport(transport)
#4 从Linux 传文件到windows,，get(’远程文件的路径‘，’本地主机文件路径‘)
#sftp_client.get('a.txt',r'F:\untitled\lll\ll.txt')
#5 从windows上传文件到linux
#sftp_client.put(r'F:\untitled\lll\ll.txt','/root/b.txt')
'''
import paramiko
transport=paramiko.Transport(('192.168.2.'))
import socket






