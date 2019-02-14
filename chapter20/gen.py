#coding=utf-8

def gensquares(N):
    for i in range(N):
        yield i**2
 
for i in gensquares(5):
    print(i,end=':')

print()
square_gen=gensquares(5)
print(square_gen.__next__())
print(next(square_gen))
print(next(square_gen))
print(next(square_gen))
print(next(square_gen))
print(square_gen)

0:1:4:9:16:
0
1
4
9
16
<generator object gensquares at 0x7f169163d2b0>
