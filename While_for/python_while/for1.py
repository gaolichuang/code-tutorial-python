#-*- coding:UTF-8 -*-
'''
Created on 2012-4-22

@author: RM
'''
#内置函数range可以返回一些列连续增加的整数，可以作为for的索引
for i in range(-4,9):
    print i
    
#并行遍历zip
L1 = [1,2,3,4]
L2 = [5,6,7,8]
z = zip(L1,L2)
print type(z)
print list(z)
for (x,y) in zip(L1,L2):
    print(x,y,'--',x+y)

#map 函数
S1 = 'abc'
S2 = 'xyz123'
L = map(None, S1,S2)
print L
#使用zip构造字典
keys = ['spam','eggs','toast']
values = [1,2,3]
D = dict(zip(keys,values))
print D


L = [1,2,3,4,5,6]
for i in range(len(L)):
    L[i] += 10
print L
