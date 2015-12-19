#-*- coding:UTF-8 -*-
'''
Created on 2012-4-22

@author: RM
'''
'''
dir函数，可以列出对象中可用的属性
文档字符串 __doc__ , 附加在对象上的文件中的文档
help函数
'''
import sys
print dir(sys)
print sys.__doc__
print dir([])
print dir('')
def fun():
    """
     fun function document here
    """
    print 'func doc'
    
print(fun.__doc__)