#coding=utf-8

import sys

def print30(*args,sep=' ',end='\n',file=sys.stdout):
    output=''
    first=True
    for arg in args:
        output+=('' if first else sep) + str(arg)
        first=False
    file.write(output+end)
    
print30("abcdefg")