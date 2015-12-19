#-*- coding:UTF-8 -*-  这样就能输入中文了
'''
Created on 2012-4-9

@author: RM
'''
print 1/3.0
a = 4 ** 2
print a
print 2 > 4, 4 > 5
print 1 == 2 < 3 # same as 1 == 2 and 2 < 3

print 10 / 4
import math
# 向下舍入
ret = math.floor(10 / 4) 
print ret
print math.floor(-2.5)
print math.trunc(-2.5)
print (5//2) #在import math之后的截断除法
print math.e
print math.pi
print math.pow(2, 4)
print abs(-874.243)
print sum((1,3,4,5,6))
print min(2,5,6,7), max(1,4,5,6)


import random
print random.random
print random.randint(1,10)

# 浮点数缺乏精度的问题
print(0.1 + 0.1 + 0.1 - 0.3)
from decimal import Decimal # 调用decimal模块中的Decimal构造函数创建一个小数对象
print(Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3'))

#设置全局精度
import decimal
print(decimal.Decimal(1) / decimal.Decimal(7))
decimal.getcontext().prec = 4
print(decimal.Decimal(1) / decimal.Decimal(7))
with decimal.localcontext() as ctx:
    ctx.prec = 2
    print(decimal.Decimal(1) / decimal.Decimal(7))
print(decimal.Decimal(1) / decimal.Decimal(7))

#分数
from fractions import Fraction
x = Fraction(1, 3)
print x
print(Fraction(1, 3) + Fraction(1, 3))  #正常运算
print(Fraction('2.5'))

#集合
x = set('abcdefg')
y = set('aceghijk')
print x
print 'a' in x  #membership
print x - y # Difference
print x|y # union
print x ^ y # XOR
print x > y, x < y #superset subset
print x | set([3, 4])
print x.issubset(range(-5, 5))