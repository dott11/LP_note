#coding=utf-8

class MetaOne(type):
    def __new__(meta, classname, supers, classdict): # Redefine type method
        print('In MetaOne.new:', classname)
        return type.__new__(meta, classname, supers, classdict)
    def toast(self):
        print('toast')
        
class Super(metaclass=MetaOne): # Metaclass inherited by subs too
    def spam(self): # MetaOne run twice for two classes
        print('spam')
        
class C(Super): # Superclass: inheritance versus instance
    def eggs(self): # Classes inherit from superclasses
        print('eggs') # But not from metclasses
X = C()
X.eggs() # Inherited from C
X.spam() # Inherited from Super
X.toast() # Not inherited from metaclass

In MetaOne.new: Super
In MetaOne.new: C
eggs
spam
Traceback (most recent call last):
  File "/root/workspace/test3/Test/test.py", line 20, in <module>
      X.toast() # Not inherited from metaclass
      AttributeError: 'C' object has no attribute 'toast'
