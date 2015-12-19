#-*- coding:UTF-8 -*-
'''
Created on 2012-4-10

@author: RM
'''

#单引号和双引号功能相同
print('test',"test")
print('some"some',"some'some")

strs = "i am "' jack' "jons"
print str
#多行的string
strs = '''fwjeoifew
fewjoij
fweijo
'''
print strs
#function
print ("str length %d" % len(strs))
print('asdf' + 'jkl;')
print('-'*10)
#索引和分片
s = 'spam'
print(s[0])
print(s[0:-1])
s = 'asdfjkl;qweruiop'
print(s[0:10:2]) #第三个参数是步长

#string 和int
s = '42'
i = 5
print(int(s) + i)
#str是内置的函数，不能随便用来作为变量
print(s + str(i))



#raw字符串抑制转义
path = r'c:\djiwe\tfew'
print path
path = 'c:\djiwe\tfew'
print path

s = 'splot'
s = s.replace('pl', 'pamal')
print s

#替换字符串
print('this is %d %s bird!' % (1, 'dead'))
print('htis is {0} {1} bird!'.format(1, 'dead'))
#这里面一切皆字符串，所以在print的时候除非特殊格式要求，都可以使用%s
print("%s %s %s" % (42, 3.23, [1,3,4]))




#function
line = 'bob,tom,jack'
col = line.split(',')
print col
print('egg'.join(['b','c','d']))
List = list(line)
print List
line = 'The knights who say Hi!\n'
print(line.rstrip())
print(line.upper())
print(line.isalpha())
print(line.endswith('Hi\n'))
print(line.startswith('the'))
print(line.find('Hi'))

#该内置函数可以将之前的变量都放到一个字典里面
print(vars())