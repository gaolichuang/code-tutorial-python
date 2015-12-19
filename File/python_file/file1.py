#-*- coding:UTF-8 -*-
'''
Created on 2012-4-22

@author: RM
'''
'''
基本操作
output = open('rC:/spam','w) 创建输出文件，w属性，写入
input = open('data','r') 创建输入文件 r属性
input = open('data') 默认是r属性的
aString = input.read() 把整个文件读进单一字符串
aString = input.read(N) 读取之后的N个字节到一个字符串
aString = input.readline() 读取一行到一个字符串，包括行末的标识符
aList = input.readlines() 读取整个文件到字符串列表
output.write(aString) 写入字节字符串到文件
output.writelines(aList) 把列表中的所有字符串写入文件
output.close()
output.flush() 把输出缓冲区的内容刷到磁盘上，但不关闭文件
for line in open('data'): use line 文件迭代器的方式一行一行的读取
python不会自动的将从文件中读出来的内容转化为python对象
'''