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
    y=MySet([5,7,9])
    print(x)
    print(y)
    print(x.union(y))
    print(x.union([11,22,33]))
    print(x&y)
    print(x.intersect(y))
    print(x.intersect([11,22,33]))
    print(x&y)

MySet:[1, 2, 3, 4, 5, 7]
MySet:[5, 7, 9]
MySet:[1, 2, 3, 4, 5, 7, 9]
MySet:[1, 2, 3, 4, 5, 7, 11, 22, 33]
MySet:[5, 7]
MySet:[5, 7]
MySet:[]
MySet:[5, 7]
