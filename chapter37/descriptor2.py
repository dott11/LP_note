#coding=utf-8

class DescState: # Use descriptor state
    def __init__(self, value):
        self.value = value
    def __get__(self, instance, owner): # On attr fetch
        print('DescState get')
        return self.value * 10
    def __set__(self, instance, value): # On attr assign
        print('DescState set')
        self.value = value
        
# Client class
class CalcAttrs:
    X = DescState(2) # Descriptor class attr
    Y = 3 # Class attr
    def __init__(self):
        self.Z = 4 # Instance attr
        
obj = CalcAttrs()
print(obj.X, obj.Y, obj.Z) # X is computed, others are not
obj.X = 5 # X assignment is intercepted
obj.Y = 6
obj.Z = 7
print(obj.X, obj.Y, obj.Z)

DescState get
20 3 4
DescState set
DescState get
50 6 7

