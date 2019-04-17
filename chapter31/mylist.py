#coding=utf-8

class MyList(list):
    def __getitem__(self, offset):
        print('(indexing %s at %s)'%(self,offset))
        return list.__getitem__(self, offset-1)

if __name__=='__main__':
    print(list('abc'))
    x=MyList('abc')
    print(x)
    print(x[1])
    print(x[2])
    print(x[3])
    for i in x:
        print(i)

['a', 'b', 'c']
['a', 'b', 'c']
(indexing ['a', 'b', 'c'] at 1)
a
(indexing ['a', 'b', 'c'] at 2)
b
(indexing ['a', 'b', 'c'] at 3)
c
a
b
c

