#-*- coding:UTF-8 -*-
'''
Created on 2012-4-15

@author: RM
'''
l = [1,2,3]
l.insert(0,0)
print l
i = 0
while i < len(l):
    print l[i]
    i+=1
exit(0)
print l
print l*4
#类型转换
s = "34"
r = str(l) + s
print r
r = l +  list(s)
print r

#membership
ret = 3 in [1,2,3]
print ret
for x in [1,3,4]:
    print(x)

#将spam转换成ssss pppp aaaa mmmm
ret = [c*4 for c in 'spam']
print ret
res =[]
for c in 'spam':
    ret.append(c*4)
print ret

#和map函数的合作
'''
map(function, sequence[, sequence, ...]) -> list

Return a list of the results of applying the function to the items of
the argument sequence(s).  If more than one sequence is given, 
 the
function is called with an argument list consisting of the 
 corresponding
item of each sequence, substituting None for missing values 
 when not all
sequences have the same length.  If the function is None, return 
 a list of
the items of the sequence (or a list of tuples if more than one 
 sequence).
'''
l = list(map(abs, [-1,2,3,-3,-6,3]))
print l

#索引和分片 原处修改
l = ['spam','Spam','SPAM']
l[1] = 'eggs'  #原处修改
print l
l[0:2] = ['eat','more']
print l
l.append('please')
print l
l.sort()
print l
l = ['abc','aBc','aBE']
l.sort()
print l
l = ['abc','aBc','aBE']
l.sort(key=str.lower)  #Normalize to lowercase
print l
l = ['abc','aBc','aBE']
l.sort(key=str.lower, reverse = True)  #Normalize to lowercase
print l
#使用内建的sort函数
l = ['abc','aBc','aBE']
ll = sorted(l, key=str.lower, reverse = True)
print l
print ll
ll = sorted([x.lower() for x in l], reverse = True)
print ll
#使用list的append和pop操作可以模拟堆栈数据结构
l = []
l.append(1)
l.append(2)
print l
le = l.pop()
print le
print l

l = ['spam','Spam','SPAM']
x = l.index('spam')
print x
ret = 'SPam' in l
print ret
print type(x)
l.insert(1,'toast')
print l
l.remove('Spam')
print l
l.pop(1)
print l

l = ['spam','Spam','SPAM']
#其他
del l[0]
print l
del l[1:]
print l
l = ['spam','Spam','SPAM']
l[1:] = []
print l