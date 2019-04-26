#coding=utf-8

def raise1():raise IndexError
def noraise():return
def raise2():raise SyntaxError

for func in (raise1,noraise,raise2):
    print('\n',func,sep='')
    try:
        try:
            func()
        except IndexError:
            print('caught IndexError')
    finally:
        print('finally run')
            

<function raise1 at 0x7f1b363e8048>
caught IndexError
finally run

<function noraise at 0x7f1b36303268>
finally run

<function raise2 at 0x7f1b36303620>
finally run
Traceback (most recent call last):
  File "/root/workspace/test3/Test/expect4.py", line 11, in <module>
      func()
        File "/root/workspace/test3/Test/expect4.py", line 5, in raise2
            def raise2():raise SyntaxError
            SyntaxError: None

