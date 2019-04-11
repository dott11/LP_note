#coding=utf-8

class Iters:
    def __init__(self,value):
        self.data=value
    def __getitem__(self,i):
        print('get[%s]'%i,end='')
        return self.data[i]
    def __iter__(self):
        print('iter=>',end='')
        self.ix=0
        return self
    def __next__(self):
        print('next:',end='')
        if self.ix==len(self.data):raise StopIteration
        item=self.data[self.ix]
        self.ix+=1
        return item
    def __contains__(self,x):
        print('contains:',end='')
        return x in self.data

if __name__=='__main__':
    X=Iters([1,2,3,4,5])
    print(3 in X)
    for i in X:
        print(i,end=' | ')
    print()
    print([i**2 for i in X ])
    print (list(map(bin,X)))
    I=iter(X)
    while True:
        try:
            print(next(I),end=' @ ')
        except StopIteration:
            break

contains:True
iter=>next:1 | next:2 | next:3 | next:4 | next:5 | next:
iter=>next:next:next:next:next:next:[1, 4, 9, 16, 25]
iter=>next:next:next:next:next:next:['0b1', '0b10', '0b11', '0b100', '0b101']
iter=>next:1 @ next:2 @ next:3 @ next:4 @ next:5 @ next:

注释掉__contains__方法
iter=>next:next:next:True
iter=>next:1 | next:2 | next:3 | next:4 | next:5 | next:
iter=>next:next:next:next:next:next:[1, 4, 9, 16, 25]
iter=>next:next:next:next:next:next:['0b1', '0b10', '0b11', '0b100', '0b101']
iter=>next:1 @ next:2 @ next:3 @ next:4 @ next:5 @ next:

再注释掉__iter__方法
get[0]get[1]get[2]True
get[0]1 | get[1]2 | get[2]3 | get[3]4 | get[4]5 | get[5]
get[0]get[1]get[2]get[3]get[4]get[5][1, 4, 9, 16, 25]
get[0]get[1]get[2]get[3]get[4]get[5]['0b1', '0b10', '0b11', '0b100', '0b101']
get[0]1 @ get[1]2 @ get[2]3 @ get[3]4 @ get[4]5 @ get[5]
