#coding=utf-8
import sys
print(sys.platform)
print(sys.getdefaultencoding())
B=b'fuck'
S='fuck'
print(B)
print(S)
print(type(B))
print(type(S))
print(B[0])
print(S[0])
print(B[1:])
print(S[1:])
print(list(B))
print(list(S))
print(bytes(S,encoding="utf-8"))
print(S.encode("ascii"))
print(str(B,encoding="utf-8"))
print(B.decode("ascii"))
S1 = '\u00c4\u00e8'
print(type(S1))
print(S1)
B1 = b'\xc4\xe8'
print(type(B1))
print(B1)
print(B1.decode('latin-1'))

linux
utf-8
b'fuck'
fuck
<class 'bytes'>
<class 'str'>
102
f
b'uck'
uck
[102, 117, 99, 107]
['f', 'u', 'c', 'k']
b'fuck'
b'fuck'
fuck
fuck
<class 'str'>
Äè
<class 'bytes'>
b'\xc4\xe8'
Äè

