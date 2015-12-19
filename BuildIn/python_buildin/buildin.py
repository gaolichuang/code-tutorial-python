#-*- coding:UTF-8 -*-
'''
Created on 2012-4-15

@author: RM
'''
l = [1,2,3]
print type(l) # 查看变量是什么类型

str = '[1,2,3]'  #这块是个string
print str[0]
L = eval(str)  #这块将其转化成了python的object
print L[1]



f = 1.0
print isinstance(f, float)

import json
class AAType(object):
    def __init__(self):
        self.XX = 'XX'
class AA(object):
    def __init__(self,name,type):
        self.name = name
        self.type = 'XX'
    def todict(self):
        return {'name':self.name,
                'type':self.type}
atype = AAType()
a = AA('who',atype)
encodejson = json.dumps(a.todict())
print type(encodejson)
print encodejson
print type('adb')
ll = json.loads(encodejson)
print type(ll)

