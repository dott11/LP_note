#coding=utf-8

class MetaOne(type):
    def __new__(meta, classname, supers, classdict):
        print('In MetaOne.new: ', classname, supers, classdict, sep='\n...')
        return type.__new__(meta, classname, supers, classdict)
    def __init__(Class, classname, supers, classdict):
        print('In MetaOne init:', classname, supers, classdict, sep='\n...')
        print('...init class object:', list(Class.__dict__.keys()))
        
class Eggs:
    pass

print('making class')
class Spam(Eggs, metaclass=MetaOne): # Inherits from Eggs, instance of Meta
    data = 1 # Class data attribute
    def meth(self, arg): # Class method attribute
        pass
print('making instance')

making class
In MetaOne.new: 
...Spam
...(<class '__main__.Eggs'>,)
...{'__module__': '__main__', '__qualname__': 'Spam', 'data': 1, 'meth': <function Spam.meth at 0x7fe3ce444ae8>}
In MetaOne init:
...Spam
...(<class '__main__.Eggs'>,)
...{'__module__': '__main__', '__qualname__': 'Spam', 'data': 1, 'meth': <function Spam.meth at 0x7fe3ce444ae8>}
...init class object: ['__module__', '__doc__', 'data', 'meth']
making instance
