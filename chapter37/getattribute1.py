#coding=utf-8

class AttrSquare:
    def __init__(self, start):
        self.value = start # Triggers __setattr__!
    def __getattribute__(self, attr): # On undefined attr fetch
        if attr == 'X':
            return self.value ** 2 # value is not undefined
        else:
            return object.__getattribute__(self, attr)
    def __setattr__(self, attr, value): # On all attr assignments
        if attr == 'X':
            attr = 'value'
#         object.__setattr__(self, attr, value)
        self.__dict__[attr]=value

A = AttrSquare(3) # 2 instances of class with overloading
B = AttrSquare(32) # Each has different state information
print(A.X) # 3 ** 2
A.X = 4
print(A.X) # 4 ** 2
print(B.X) # 32 ** 2
A.name=213
print(A.__dict__)
print(A.name)

9
16
1024
{'value': 4, 'name': 213}
213

构造函数中的self.value=start 触发__setattr__。
__getattribute__中self.value再次触发__getattribute__。
实际上，每次我们获取属性X的时候，__getattribute__都运行了两次。
