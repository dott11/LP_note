#coding=utf-8

def d1(F):
    print("d1") 
    return lambda: 'X' + F()
def d2(F):
    print("d2") 
    return lambda: 'Y' + F()
def d3(F): 
    print("d3")
    return lambda: 'Z' + F()

@d1
@d2
@d3
def func():
    return "spam"

print(func())

d3
d2
d1
XYZspam
