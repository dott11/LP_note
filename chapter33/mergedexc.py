#coding=utf-8

sep='-'*32+'\n'
print(sep+'EXCEPTION RAISED AND CAUGHT')
try:
    x='sapm'[99]
except IndexError:
    print('except run')
finally:
    print('finally run')
print('after run')

print(sep+'NO EXCEPTION RAISED')
try:
    x='spam'[3]
except IndexError:
    print('except run')
finally:
    print('finally run')
print('after run')

print(sep+'NO EXCEPTION RAISED,WITH ELSE')
try:
    x='spam'[3]
except IndexError:
    print('except run')
else:
    print('else run')
finally:
    print('finally run')
print('after run')

print(sep+'EXCEPTION RAISED BUT NOT CAUGHT')
try:
    x=1/0
except IndexError:
    print('except run')
finally:
    print('finally run')
print('after run')

--------------------------------
EXCEPTION RAISED AND CAUGHT
except run
finally run
after run
--------------------------------
NO EXCEPTION RAISED
finally run
after run
--------------------------------
NO EXCEPTION RAISED,WITH ELSE
else run
finally run
after run
--------------------------------
EXCEPTION RAISED BUT NOT CAUGHT
finally run
Traceback (most recent call last):
  File "/root/workspace/test3/Test/mergedexc.py", line 35, in <module>
      x=1/0
      ZeroDivisionError: division by zero
