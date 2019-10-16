#!/usr/bin/python
#-*-coding:utf-8-*-

#请求网址
# import re
# import requests
# a='https://sou.zhaopin.com/?p=2&jl=765&kw=软件测试工程师&kt=3&sf=0&st=0'
# b=requests.get(a)
# print(b)

'''  接收响应内容第一种text，以unicode的方式接收'''
# c=b.text  不常用
# print(c)

'''接收响应内容第二种content，以字节的方式接收'''
# c=b.content
# print(c)
# c=b.content.decode('gbk')    #.decode()：解码，要先看网页源代码是什么编码方式然后输入括号里
# guolv=re.compile('</script>&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<div class="backs">',re.S)
# answer=guolv.findall(c)
# print(answer)
# for i in answer:
#      b=i.strip('&nbsp;&nbsp;&nbsp;&nbsp;')
#      print(b)


# with open('视频下载.mp4','wb') as a:     将其存放在，，，，
#      a.write(c)

# import re
# zifu='4werqe\nSGhg  123qFw4q'
# guolv=re.compile('q(.*)q',re.S)
# answer=re.findall(guolv,zifu)
# answer1=guolv.findall(zifu)
# print(answer)

#爬地图

# import requests
# import json
# url='https://map.baidu.com/?qt=subwayscity&t=1569031922131'
# head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}     #简单的反爬的
# html=requests.get(url,headers=head)
# geshi=html.text
# result=json.loads(geshi)
# i=0
# while True:
#     try:
#         city=result['subways_city']['cities'][i]['cn_name']
#         print(city)
#         i+=1
#     except:
#         break
# a=open('1.txt','wb',encoding='utf8')


#招聘
# import re
# import requests
# import json
# url='https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=765&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=软件测试工程师&kt=3&_v=0.85683604&x-zp-page-request-id=f45b58ec29464130bcd6cdf2869c9b6a-1569204955090-545032&x-zp-client-id=ae59f9c2-bfa2-4507-9cd5-18a2c1bb60b9'
# head={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'}     #简单的反爬的
# html=requests.get(url,headers=head)
# geshi=html.text
# result=json.loads(geshi)
# a=result['data']['results']
# for i in range(len(a)):
#     b=result['data']['results'][i]['company']['name']
#     print(b)
# import xlwt
# xl=xlwt.Workbook(encoding='utf8')
# y=xl.add_sheet('t_test')
# y.write(0,0,i)
# xl.save('a.xls')






# for i in range(len(resurt))
# print(i)
#
# a=open('11.txt','wb',encoding='ansi')
# a='https://sou.zhaopin.com/?jl=765&kw=软件测试工程师&kt=3&sf=0&st=0'
# b=requests.get(a)
# print(b)

# c=b.content.decode('utf8')
# guolv=re.compile('<div id="collect_form_27010768"></div>(.*?)<span class="box_chart_num color-gray">185万</span>',re.S)
# answer=guolv.findall(c)
# print(answer)
# with open('11.txt','w',encoding='ansi') as s:
#     s.write(result)


