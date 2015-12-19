#-*- coding:UTF-8 -*-
'''
Created on 2012-4-22

@author: RM
'''
#内置的方法
f = open('data.txt')
f.__next__()
f.__next__()
f.close()

f = open('data.txt')
next(f)
next(f)

L = [1,2,3]
I = iter(L)
print I.next()
print I.next()
print I.next()
print I.next()