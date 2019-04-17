#coding=utf-8

class newprops():
    def getage(self):
        return 40
    def setage(self,value):
        print('set age:',value)
        self._age=value
    age=property(getage,setage,None,None)

class classic:
    def __getattr__(self,name):
        if name=='age':
            return 41
        else:
            raise AttributeError
    def __setattr__(self,name,value):
        print('set:',name,value)
        if name=='age':
            self.__dict__['_age']=value
        else:
            self.__dict__[name]=value
    
if __name__=='__main__':
    x=newprops()
    print(x.age)
    x.age=42
    print(x._age)
    x.job='trainer'
    print(x.job)
    print(x.__dict__)
    print()
    y=classic()
    print(y.age)
    y.age=43
    print(y._age)
    y.job='worker'
    print(y.job)
    print(y.__dict__)

40
set age: 42
42
trainer
{'job': 'trainer', '_age': 42}

41
set: age 43
43
set: job worker
worker
{'job': 'worker', '_age': 43}

