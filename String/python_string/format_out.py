#-*- coding:UTF-8 -*-
'''
Created on 2012-4-15
#-*- coding:UTF-8 -*-
@author: RM
'''
#格式化输出
#左对齐，右对齐，
x  = 1234
print('integers:%d...%-6d...%06d' % (x, x, x))
x = 1.23456789
print x
print('%-6.2f | %05.2f | %+06.1f' % (x, x, x))
#给予字典的格式化输出
print("%(n)d %(x)s" % {"n":1, "x":"spam"})
reply = '''
greetings...
hello %(name)s!
your age is %(age)s
'''
value = {'name':"jack", 'age':30}
print(reply % value)

name = "tom"
age = 25
print("%(name)s %(age)d " % vars()) #这种方式很有用！可以将之前的变量集中到一个字典里卖弄

template = '{0}, {1} and {2}' # by position
print template.format('spam', 'ham', 'eggs')


X = '{motto}, {0} and {food}'.format(42, motto = 3.14, food = [1,2])
print X
print X.split(' and ')
Y = X.replace('and', 'but under no circumstances')
#format的时候可以使用关键字，属性
import sys
#这个是通过索引来访问参数列表
X = 'My {1[spam]} runs {0.platform}'.format(sys, {'spam': 'laptop'})
print X
#通过键值访问参数列表
X = 'My {config[spam]} runs {sys.platform}'.format(sys = sys, config={'spam':'laptop'})
#列表作为参数，也可以通过索引来访问
somelist = list('spam')
print somelist
X = 'first={0[0]}, third = {0[2]}'.format(somelist)
print X
X = 'first={0}, last = {1}'.format(somelist[0],somelist[-1])
print X
parts = somelist[0],somelist[1],somelist[1:3]
X = 'first={0}, second = {1},middle={2}'.format(*parts)
print X
#还有更多对其方式等使用，这个在参考吧。。。
print '{0:10} = {1:10}'.format('spam', 123.456)
print '{0:>10} = {1:<10}'.format('spam', 123.456)
#不同进制之间转换
print '{0:X}, {0:o}, {0:b}'.format(255)
print bin(255), int('11111111', 2), 0b11111111
print hex(255), int('FF', 16), 0xFF
print oct(255), int('377', 8), 0o377,0377

#使用百分号的方法
template = '%s %s %s'   # by position
r = template % ('spam', 'ham', 'eggs')
print r
template = '%(motto)s, %(pork)s, %(food)s' # by key
r = template % dict(motto = 'spam', pork = 'ham', food='eggs')
print r
print '%s,%s,%s' % (2.14, 42, [1,2]) # Arbitrary types

somelist = list('spam')
parts = somelist[0],somelist[-1],somelist[1:3]
r = 'first=%s, last=%s, middle=%s' % parts
print r
