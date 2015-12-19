#-*- coding:UTF-8 -*-
'''
Created on 2012-4-22

@author: RM
'''
'''
元组
1.任意对象的有序集合
类似于列表，
2.通过偏移量存储
3.属于不可变类型
这个和列表就不同了
4.固定长度，异构，任意嵌套
因为元组是不可变的，所以在不生成拷贝的情况下是不能增长和缩短的
5.对象引用的数组
元组存储指向其他对象的引用
'''
'''
基本操作
() 空元组
T = (0,) 有单个元素的元组
T = (0, 'Ni', 1.2, 3) 四个元素的元组
T = 0, 'Ni', 1.2, 3 另一种方式
T = ('abc', ('def','ghi'))  元组的嵌套
T = tuple('spam')
T[i]    索引
T[i][j]
T[i:j]
len(T)
T1 + T2 合并，重复
T * 3
for x in T: print x  迭代，成员关系
'spam' in T
[x**2 for x in T]
T.index('Ni')
T.count('Ni')
'''
'''
元组的不可变性可以确保元组在程序中不被另一个引用修改，也就是const
'''

help(tuple)