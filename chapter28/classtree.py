#coding=utf-8
"""
Climb inheritance trees using namespace links,
displaying higher superclasses with indentation
"""

def classtree(cls,indent):
    print('.'*indent+cls.__name__)
    for supercls in cls.__bases__:
        classtree(supercls,indent+3)

def instancetree(inst):
    print('Tree of %s'%inst)
    classtree(inst.__class__,3)

def selftest():
    class A:    pass
    class B(A): pass
    class C(A): pass
    class D(B,C):   pass
    class E:    pass
    class F(D,E):   pass
    instancetree(A())
    instancetree(B())
    instancetree(C())
    instancetree(D())
    instancetree(E())
    instancetree(F())

if __name__=='__main__':
    selftest()

Tree of <__main__.selftest.<locals>.A object at 0x7f9bfbc30cc0>
...A
......object
Tree of <__main__.selftest.<locals>.B object at 0x7f9bfbc30cc0>
...B
......A
.........object
Tree of <__main__.selftest.<locals>.C object at 0x7f9bfbc30cc0>
...C
......A
.........object
Tree of <__main__.selftest.<locals>.D object at 0x7f9bfbc30cc0>
...D
......B
.........A
............object
......C
.........A
............object
Tree of <__main__.selftest.<locals>.E object at 0x7f9bfbc30cc0>
...E
......object
Tree of <__main__.selftest.<locals>.F object at 0x7f9bfbc30cc0>
...F
......D
.........B
............A
...............object
.........C
............A
...............object
......E
.........object

