#-*- coding:UTF-8 -*-
'''
Created on 2012-4-22

@author: RM
'''

x = (40)  #x是一个整数
print x
y = (40,) #y是一个元组
print y

#类型转化
T = ('a','b','c','d','e',)
tmp = list(T)
tmp.sort()
T = tuple(tmp)
print T
T = (1,2,3,4,5)
L = [x + 20 for x in T]
print L
T = (1,2,3,2,3,4,5,2)
print T.index(2)
print T.index(2,2) # 第二个2的index
print T.count(2) # 出现了多少个2
