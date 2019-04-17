#coding=utf-8

class MySet:
    def __init__(self,value=[]):
        self.data=[]
        self.concat(value)
    def concat(self,value):
        for x in value:
            if not x in self.data:
                self.data.append(x)
    def intersect(self,other):
        return MySet([x for x in self.data if x in other])
    def union(self,other):
        res=self.data[:]
        for x in other:
            if not x in res:
                res.append(x)
        return MySet(res)
    def __len__(self):
        return len(self.data)
    def __getitem__(self,key):
#         print("getitem")
        return self.data[key]
    def __and__(self,other):
        return self.intersect(other)
    def __or__(self,other):
        return self.union(other)
    def __repr__(self):
        return 'MySet:'+repr(self.data)

if __name__=='__main__':
    x=MySet([1,2,3,4,5,7])
#     y=MySet([5,7,9])
#     print(x)
#     print(y)
#     print(x.union(y))
#     print(x.union([11,22,33]))
#     print(x&y)
#     print(x.intersect(y))
#     print(x.intersect([11,22,33]))
#     print(x&y)
    print(MySet.__bases__)
    print(x.__class__)
    print(x.__dict__)
    print(x.__class__.__dict__)
    print(x.__class__.__name__)
    print(getattr(x, "union"))
    union_func=getattr(x, "union")
    print(union_func([44]))

(<class 'object'>,)
<class '__main__.MySet'>
{'data': [1, 2, 3, 4, 5, 7]}
{'__len__': <function MySet.__len__ at 0x7ff84690cbf8>, '__dict__': <attribute '__dict__' of 'MySet' objects>, '__init__': <function MySet.__init__ at 0x7ff8469ba268>, 'intersect': <function MySet.intersect at 0x7ff84690cae8>, '__weakref__': <attribute '__weakref__' of 'MySet' objects>, '__repr__': <function MySet.__repr__ at 0x7ff84690ce18>, 'concat': <function MySet.concat at 0x7ff8469ba620>, '__module__': '__main__', '__getitem__': <function MySet.__getitem__ at 0x7ff84690cc80>, '__doc__': None, '__or__': <function MySet.__or__ at 0x7ff84690cd90>, '__and__': <function MySet.__and__ at 0x7ff84690cd08>, 'union': <function MySet.union at 0x7ff84690cb70>}
MySet
<bound method MySet.union of MySet:[1, 2, 3, 4, 5, 7]>
MySet:[1, 2, 3, 4, 5, 7, 44]
