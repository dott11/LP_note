#coding=utf-8

def gensquares(N):
    for i in range(N):
        x=yield i**2
        print(x)
 
G=gensquares(5)
print(next(G))
print(G.send(77))
print(G.send(88))
print(next(G))
print(next(G))
print(next(G))

0
77
1
88
4
None
9
None
16
None
Traceback (most recent call last):
  File "/root/workspace/test3/Test/test.py", line 14, in <module>
      print(next(G))
      StopIteration

