#coding=utf-8
class ListInstance:
    '''
        Mix-in class that provides a formatted print() or str() of instance via inheritance of __str__,
        coded here;displays instance attrs only;self is the instance of lowest class;uses __X names to
        avoid clashing with client's attrs
    '''
    def __attrnames(self):
        result=''
        for attr in sorted(self.__dict__):
            result+='\tname %s=%s\n'%(attr,self.__dict__[attr])
        return result
    def __str__(self):
        return '<Instance of %s,address %s:\n%s>'%(self.__class__.__name__,id(self),self.__attrnames())

if __name__=='__main__':
    obj1=ListInstance()
    obj1.a='a'
    print(obj1.__dict__)
    print(obj1)

