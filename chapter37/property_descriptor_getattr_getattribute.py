#coding=utf-8

class PropertyPower:
    def __init__(self,square,cube):
        self._square = square
        self._cube = cube
    def getSquare(self):
        return self._square**2
    def setSquare(self,value):
        self._square=value
    square=property(getSquare,setSquare)
    def getCube(self):
        return self._cube**3
    cube=property(getCube)
    
class SquareDescriptor:
    def __get__(self,instanse,owner):
        return instanse._square**2
    def __set__(self,instanse,value):
        instanse._square=value

class CubeDescriptor:
    def __get__(self,instance,owner):
        return instance._cube**3
    
class DescriptorPower():
    square=SquareDescriptor()
    cube=CubeDescriptor()
    def __init__(self,square,cube):
        self._square = square
        self._cube = cube

class GetattrPower():
    def __init__(self,square,cube):
        self._square = square
        self._cube = cube
    def __getattr__(self,attr):
        if attr=="square":
            return self._square**2
        elif attr=="cube":
            return self._cube**3
        else:
            raise AttributeError(attr)
    def __setattr__(self,attr,value):
        if attr=="square":
            attr="_square"
        self.__dict__[attr]=value

class GetattributePower():
    def __init__(self,square,cube):
        self._square = square
        self._cube = cube
    def __getattribute__(self,attr):
        if attr=="square":
            return object.__getattribute__(self,"_square")**2
        elif attr=="cube":
            return object.__getattribute__(self,"_cube")**3
        else:
            return object.__getattribute__(self,attr)
    def __setattr__(self,attr,value):
        if attr=="square":
            attr="_square"
        self.__dict__[attr]=value

def test(func):
    power=func(3,3)
    print(power.cube)
    print(power.square)
#     power.cube=6
    power.square=6
    print(power.cube)
    print(power.square)
    print(power.__dict__)

if __name__=='__main__':
    test(PropertyPower)
    test(DescriptorPower)
    test(GetattrPower)
    test(GetattributePower)
            
