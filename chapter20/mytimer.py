#coding=utf-8
import sys,time

reps1=1000
repslist1=range(reps1)
reps2=10000
repslist2=range(reps2)

def timer(func,*pargs,**kargs):
    start=time.clock()
    for i in repslist1:
        ret=func(*pargs,**kargs)
    elapsed=time.clock()-start
    return (elapsed,ret)

def forLoop():
    res=[]
    for x in repslist2:
        res.append(abs(x))
    return res

def listComp():
    return[abs(x) for x in repslist2]

def mapCall():
    return list(map(abs,repslist2))

def genExpr():
    return list(abs(x) for x in repslist2)

def genFunc():
    def gen():
        for x in repslist2:
            yield abs(x)
    return list(gen())

print(sys.version)
for test in (forLoop,listComp,mapCall,genExpr,genFunc):
    elapsed,result=timer(test)
    print('-'*33)
    print("%-9s:%.5f=>[%s...%s]"%(test.__name__,elapsed,result[0],result[-1]))


3.5.3 (default, Sep 27 2018, 17:25:39) 
[GCC 6.3.0 20170516]
---------------------------------
forLoop  :4.08145=>[0...9999]
---------------------------------
listComp :2.35977=>[0...9999]
---------------------------------
mapCall  :2.00443=>[0...9999]
---------------------------------
genExpr  :3.01156=>[0...9999]
---------------------------------
genFunc  :2.95123=>[0...9999]
