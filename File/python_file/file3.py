#-*- coding:UTF-8 -*-
'''
Created on 2012-4-22

@author: RM
'''
#shiyong pickle
import pickle
D = {'a':1,'b':2}
F = open('datafile.pk1','wb')
pickle.dump(D, F)
F.close()

F = open('datafile.pk1','rb')
E = pickle.load(F)
print E

#读取文件的一般方式
myfile = open('datafile.txt')
try:
    for line in myfile:
        # .... use line
        print
finally:
    myfile.close()