#coding=utf-8
import time

class timer:
    def __init__(self, func):
        self.func = func
        self.alltime = 0
    def __call__(self, *args, **kargs):
        start = time.clock()
        result = self.func(*args, **kargs)
        elapsed = time.clock() - start
        self.alltime += elapsed
        print('%s: %.5f, %.5f' % (self.func.__name__, elapsed, self.alltime))
        return result

@timer
def listcomp(N):
    return [x * 2 for x in range(N)]

@timer
def mapcall(N):
    return list(map((lambda x: x * 2), range(N)))

@timer
def forloop(N):
    res=[]
    for x in range(N):
        res.append(x*2)
    return res

@timer
def genexpr(N):
    return list(x * 2 for x in range(N))

@timer
def genfunc(N):
    def gen(N):
        for x in range(N):
            yield x*2
    return list(gen(N))

def test(func):
    result = func(5) 
    func(50000)
    func(500000)
    func(5000000)
    print(result)
    print('allTime = %s' % func.alltime) 
    print('')

if __name__=="__main__":
    test(listcomp)
    test(mapcall)
    test(forloop)
    test(genexpr)
    test(genfunc)

listcomp: 0.00001, 0.00001
listcomp: 0.00813, 0.00814
listcomp: 0.10557, 0.11371
listcomp: 1.06420, 1.17791
[0, 2, 4, 6, 8]
allTime = 1.177908

mapcall: 0.00002, 0.00002
mapcall: 0.01768, 0.01770
mapcall: 0.18155, 0.19924
mapcall: 1.85273, 2.05198
[0, 2, 4, 6, 8]
allTime = 2.051976

forloop: 0.00001, 0.00001
forloop: 0.01749, 0.01750
forloop: 0.18765, 0.20515
forloop: 1.92495, 2.13010
[0, 2, 4, 6, 8]
allTime = 2.1300989999999995

genexpr: 0.00002, 0.00002
genexpr: 0.01268, 0.01270
genexpr: 0.14302, 0.15572
genexpr: 1.48727, 1.64298
[0, 2, 4, 6, 8]
allTime = 1.6429820000000017

genfunc: 0.00001, 0.00001
genfunc: 0.01463, 0.01464
genfunc: 0.12362, 0.13826
genfunc: 1.41324, 1.55150
[0, 2, 4, 6, 8]
allTime = 1.551495000000001

