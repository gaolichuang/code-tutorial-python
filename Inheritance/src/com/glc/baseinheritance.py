# -*- coding: utf-8 -*-
'''
Created on 2014.1.1

@author: gaolichuang
'''

class base(object):
    def __init__(self,who):
        self.who = who
        print('I am %s in base'% self.who)
    def function1(self):
        print('I am in base function1')
    def whoarey(self):
        print('i am base %s'%self.who)
        
class subclass(base):
    def function1(self):
        super(subclass,self).function1()
        print('i am in subclass fuction1')
        
if __name__ == '__main__':
    b = subclass('gg')
    b.function1()
    b.whoarey()