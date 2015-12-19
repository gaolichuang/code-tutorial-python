# -*- coding: utf-8 -*-
'''
Created on 2014.1.1

@author: gaolichuang
'''

import inspect

def caller_name(skip=2):
    """Get a name of a caller in the format module.class.method
    
       `skip` specifies how many levels of stack to skip while getting caller
       name. skip=1 means "who calls me", skip=2 "who calls my caller" etc.
       
       An empty string is returned if skipped levels exceed stack height
    """
    stack = inspect.stack()
    start = 0 + skip
    if len(stack) < start + 1:
      return ''
    parentframe = stack[start][0]    
    
    name = []
    module = inspect.getmodule(parentframe)
    # `modname` can be None when frame is executed directly in console
    # TODO(techtonik): consider using __main__
    if module:
        name.append(module.__name__)
    # detect classname
    if 'self' in parentframe.f_locals:
        # I don't know any way to detect call from the object method
        # XXX: there seems to be no way to detect static method call - it will
        #      be just a function call
        name.append(parentframe.f_locals['self'].__class__.__name__)
    codename = parentframe.f_code.co_name
    if codename != '<module>':  # top level usually
        name.append( codename ) # function or a method
    del parentframe
    return ".".join(name)

class abase(object):
    def who(self,i):
       # print caller_name()
        print('XXXX %s'%i)
        print base.__class__.__name__
        print self.__class__.__name__
class base(abase):
    def print1(self):
        fuc = getattr(self,'who')
        fuc('oooo')
 

    

if __name__ == '__main__':
    b = base()
    print inspect.getmembers(b.who)

    b.print1()
    print b.__class__.__name__
