#!/usr/bin/python
#-*-coding:utf-8-*-
# import paramiko
# transport=paramiko.Transport(('192.168.47.103',22))
# transport.connect(username='root',password='123456')
# sftp_client=paramiko.SFTPClient.from_transport(transport)
# sftp_client.get('/root/2.txt',r'F:\untitled\lll\v.txt')
# sftp_client.put(r'F:\untitled\lll\1.txt','2.txt')

# import os
# aa=os.popen('ping 192.168.47.103')
# print(aa.read())
# print(os.chdir())
# os.chdir('C:')
# print(os.getcwd())
# os.mkdir('ss')
# os.removedirs('dd/ff/gg')
# os.rmdir('ss')
# print(os.listdir('C:'))
# aa=os.path.isfile(r'F:\untitled\lll\1.txt')
# print(aa)


#excel写入数据库
# import xlwt
# import pymysql
# xw = xlwt.Workbook('utf-8')
# sheet = xw.add_sheet('第一页')
# conn = pymysql.connect(host='192.168.47.103',port=3306,user='root',passwd='123456')
# cursor = conn.cursor()
# cursor.execute('select * from bb;')
# a = cursor.fetchall()pip
# for i,j in enumerate(a):
#     for m,n in enumerate(j):
#        print(m,n)
#        sheet.write(i,m,n)
# xw.save('shu.xls')
