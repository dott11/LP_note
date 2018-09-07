#coding=utf-8

def intersect(s1,s2):
    L=[]
    for x in s1:
        if x in s2:
            L.append(x)
    return L

s1="abcd"
s2="abc"
list1=intersect(s1, s2)
print(list1)

print([x for x in s1 if x in s2])