#!/usr/bin/python
#-*-coding:utf-8-*-
'''
import pymysql
                                                                                           #用来连接与操作数据库的
conn=pymysql.connect(host='192.168.2.131',port=3306,user='root',passwd='123456',db='mysql')#这一条是连接数据库
 #可以写成 ('192.168.2.120','3306','root','123456'这时候按顺序的话就不用写前面的名字，它默认知道哪个是哪个)                                                                     #(主机ip，用户名，端口号密码数据库)
                                                                                           # db(database)是选择数据库，
                                                                                           # 这个有了之后下面就不用再选择了
                                                                                           #charset是数据库统一编码，可以修改

#设置游标（暂存结果）
haha=conn.cursor()

#执行sql语句
#haha.execute('use mysql')  #这个是选择数据库的，这个有了就不用上面那个
haha.execute('show databases;')
#haha.execute('create table biaoming(name char);') #创建一个表，这时候可以去数据库里
                                                  # 查看下是否有这个表，其实里面已经有了
haha.execute('show tables')
print(haha.fetchall())#查看上一句sql语句的执行结果
haha.execute('show tables')
print(haha.fetchmany(2))#默认只显示一个结果的第一个值,数字是你想显示几个值你写几
conn.commit() #提交数据
conn.close()  #断开连接
'''




#链接不上数据库：在虚拟机上--编辑--网络编辑器--自动选择选择自己主机上的网卡适配器，
'''
import pymysql
class Mysql_learn(object):
    def __init__(self):
        self.conn=pymysql.connect(host='192.168.2.120',port=3306,user='root',passwd='123456',db='mysql')

        self.su=self.conn.cursor()
    def cao_zuo(self):
        #执行sql语句  execute
        self.su.execute('show databases;')
        self.su.execute('use mysql;')
        self.su.execute('show tables;')
        self.su.execute('select * from kk')
        #self.su.execute('drop table kk;')
        self.su.execute('create table ii(`name` char(20),`sex` char(20),`age` int(20),`pro` char(20));')
        #self.su.execute('insert into kk values("李川",20);')

        # for i in range(10):                   # 添加一百条数据
        #      print(self.su.execute('insert into kk values ("李川",20);'))

        #读取上一个sql语句执行的结果
        # fetchall  读取所有内容
        # fetchmany多条内容（默认是一条，括号里写几就读取几条）
        # fetchone 读取一条内容，写一个fetchone就读取一个，多写几个读几个
        #他们都具有迭代功能，
        print(self.su.fetchall ())
        #print(self.su.fetchone())

        #提交数据，只是针对某个表的数据进行添加（insert）删除（delete）更改（update）
        self.conn.commit()
        #断开连接
        self.conn.close()


d= Mysql_learn()
d.cao_zuo()
'''




