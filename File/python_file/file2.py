#-*- coding:UTF-8 -*-
'''
Created on 2012-4-22

@author: RM
'''
X, Y, Z = 43,44,45
S = 'Spam'
D = {'a':1,'b':2}
L = [1,2,3]
F = open('datafile.txt','w')
F.write(S + '\n')
F.write('%s,%s,%s\n' % (X,Y,Z))
F.write(str(L) + '$' + str(D) + '\n')
F.close

chars = open('datafile.txt').read()
print chars
print(chars)

F = open('datafile.txt')
line = F.readline()
print line
line.rstrip()
print line
line = F.readline()
parts = line.split(',')
print parts
print int(parts[1])
numbers = [int(P) for P in parts]
print numbers

line = F.readline()
print line
parts = line.split('$')
print eval(parts[0])  #将字符串转化成object
objects = [eval(p) for p in parts]
print objects
