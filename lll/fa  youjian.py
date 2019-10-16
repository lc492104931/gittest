#!/usr/bin/python
#-*-coding:utf-8-*-
#发送邮件   smtplib
import smtplib     #封装smtp协议
import email.mime.text   #处理正文中的数据
import email.mime.multipart   #封装的是邮件格式

sender='lichuan492104931@163.com'   #定义一个发送者
reser='492104931@qq.com' #定义一个接收者-------把接收者加上中括号形成列表，可以多人发送
server='smtp.163.com'        #服务器
passwd='qwert123'           #授权码,设置--

mseeage=email.mime.multipart.MIMEMultipart()   #创建一个空邮件
#添加发件人，收件人，主题
mseeage['From']=sender
mseeage['To']=''.join(reser)  #这样可以多人发送
mseeage['Subject']='python_learn'
aa="""你是俺类人
"""
cc=email.mime.text.MIMEText(aa)   #对aa进行处理
mseeage.attach(cc)     #将正文添加到邮件中

#【想发送两个附件的话就把这三步再复制一下】
#定义发送的附件的文件名，文件可以是任何格式的文件,,,加照片的话就是把照片路径复制这里
att1 = email.mime.text.MIMEText(open('F:\\untitled\视频下载.mp4', 'rb').read(), 'base64', 'utf-8')

#附件携带的字段和值
att1["Content-Type"]='a.pplication/octet-stream'
#附件携带的字段和值  这里的filename是邮件接收方接收到那边显示的名字，可以任意写，写什么名字，对方邮件中显示什么名字
att1["Content-Disposition"]='attachment;filename="a.mp4"'
#将附件添加到邮件里
mseeage.attach(att1)
#
smtp123=smtplib.SMTP_SSL(server,465)    #定义发送邮件的服务器和端口号
smtp123.login(sender,passwd)     #登录服务器
smtp123.sendmail(sender,reser,mseeage.as_string())   #发送邮件，发送的邮件用as_string去处理
#断开连接
smtp123.close()

