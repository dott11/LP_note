#coding=utf-8
class ListInherited:
    '''
        use dir() to collect both instance attrs and names inherited form its classes;python 3.0 shows more
        names than 2.6 because of the implied object superclass in the new-style class model;getattr() fetches 
        inherited names not in self.__dict__;use __str__,not __repr__ , or else ths loops when printing bound methods!
    '''
    def __attrnames(self):
        result=''
        for attr in dir(self):
            if attr[:2]=='__' and attr[-2:]=='__':
                result += '\tname %s=<>\n'%attr
            else:
                result +='\tname %s=%s\n'%(attr,getattr(self, attr))
        return result
    def __str__(self):
        return '<Instance of %s,address %s:\n%s>'%(self.__class__.__name__,id(self),self.__attrnames())
    def sup(self):
        pass
    
class Sub(ListInherited):
    def sub(self):
        pass
if __name__=='__main__':
#     obj1=ListInherited()
    obj1=Sub()
    obj1.a='a'
    print(obj1.__dict__)
    print(obj1)
    