#-*- coding:UTF-8 -*-
'''
Created on 2012-4-10

@author: RM
'''
#引用和复制
L = [1,2,3]
M = L
print(L == M)
print(L is M)
N = [1,2,3]
print(L == N)
print(L is N)
'''
类型属于对象，而不属于变量
'''
a = 3
b = a # 可以理解b是a的引用
a = 'some'
print a
print b