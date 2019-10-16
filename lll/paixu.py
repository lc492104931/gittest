#!/usr/bin/python
#-*-coding:utf-8-*-
def paixu(*args):
    a=list(args)
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
    print(a)
#paixu(12,23,21)