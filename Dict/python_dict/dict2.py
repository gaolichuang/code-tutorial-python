#-*- coding:UTF-8 -*-
'''
Created on 2012-4-15

@author: RM
'''
D = {'eggs' : 3, 'ham' : 1, 'spam' :2}
print D
print D.get('eggs')
D2 = {'toast':4, 'muffin':5}
D.update(D2)
print D
print D.pop('spam')
print D
#使用字典模拟列表，因为字典的key可以使数字
D = {}
D[99] = 'spam'
print D

#使用字典表达稀疏数据结构,这种貌似很常用！！用元组作为key来存储！！
Matrix = {}
Matrix[(2,3,4)] = 88
Matrix[(7,8,9)] = 23
print Matrix
x = 2; y = 3; z = 4;
print Matrix[(x, y, z)]
#这种情况经常会遇到读取的键值不存在的情况，所以需要提前判断键值是否存在
if (2,3,5) in Matrix:
    print(Matrix[(2,3,6)])
else:
    print(0)

try:
    print(Matrix[(2,3,6)])
except KeyError:
    print(0)

Matrix.get((2,3,6),0)
#上面三种不同的方式，用来访问稀疏矩阵！！

#创建字典的方法
D = {1:'a',2:'b'}
print D

D = {}  # 动态创建字典
D[1]='a'
D[2]='b'
#D = dict(1='a',2='b') 这种方式不行，会出错！！！
D = dict(name='Bob', age=42)
print D
D = dict([(1,'2'),(2,'b')])
print D
print D.keys()  #D字典的所有key
print D.values()  #D字典的所有value，返回的是列表

#将字典中内容按照key排序

D = {'a' : 1, 'c' : 2, 'b' : 4, 'd' : 3}
print D
Ks = D.keys()
Ks = list(Ks)
Ks.sort()
for k in Ks:
    print(k, D[k])
print([[5]]*5)




