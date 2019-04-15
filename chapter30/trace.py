#coding=utf-8

class wrapper:
    def __init__(self,object):
        self.wrapped=object
    def __getattr__(self,attrname):
        print('trace:',attrname)
        return getattr(self.wrapped, attrname)

if __name__=='__main__':
    x=wrapper([1,3,5])
    x.append(7)
    print(x.wrapped)

trace: append
[1, 3, 5, 7]
