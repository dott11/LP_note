#coding=utf-8

G=(x**2 for x in range(4))
print(G)
print(next(G))
print(next(G))
print(next(G))
print(next(G))
print(next(G))

<generator object <genexpr> at 0x7f63e52f82b0>
0
1
4
9
Traceback (most recent call last):
  File "/root/workspace/test3/Test/test.py", line 9, in <module>
    print(next(G))
StopIteration
