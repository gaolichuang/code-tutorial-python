#-*- coding:UTF-8 -*-
'''
Created on 2012-4-15

@author: RM
'''
'''
字典特性
字典是无序的集合，和list相比主要是通过键值来索引的，列表主要是通过偏移来索引的
1.通过键值来索引
字典可以理解为关联数组或者是散列表，
2.任意对象的无序集合
3.可变长，异构，任意嵌套
4.可变映射类型
通过给索引赋值，可以在字典原处修改，但不支持序列操作，
5.对象引用表
字典中存储的是引用，而不是对象本身

常用操作
D = {} 空字典
D = {'spam':2, 'eggs':2} 两个项目的字典
D = {'food':{'ham':1,'egg':2}} 嵌套
D = dict.fromkeys(['a','b'])
D = dict(zip(keyslist,valslist))  关键字，对应的对，键列表
D = dict(name='Bob', age=42)
D ['eggs'] 用键进行索引
D ['foods']['ham']
'eggs' in  D   键值存在测试
D.keys()     key的列表，返回的是列表
D.values()
D.items()  返回列表，元组队，是key和value
D.copy()
D.get(key,default)
D.update(D2)  合并
D.pop(key)   删除
len(D)   长度
D[key] = 42  新增，修改键
del D [key] 根据键删除条目
D1.keys() & D2.keys()
'''
help(dict)

'''
字典用法:
1.序列运算无效
比如合并，分片操作无效
2.对新索引赋值会添加项
如果键值不存在，则新建插入
3.键不一定总是字 符串
任何不可变的对象都可以作为键值，比如整数，使用整数会让字典看起来像列表，
'''
