#coding=utf-8
import sys, traceback

class MyError(Exception): pass

def oops():    
    raise MyError('Spam!')

def doomed():    
    try:        
        oops()    
    except IndexError:        
        print('caught an index error!')    
    except MyError as data:        
        print('caught error:', MyError, data)    
    else:        
        print('no error caught...')

doomed()

def safe(entry, *args):    
    try:        
        entry(*args)    # Catch everything else    
    except:        
        traceback.print_exc()        
        print('Got', sys.exc_info()[0], sys.exc_info()[1])

safe(oops)

caught error: <class '__main__.MyError'> Spam!
Traceback (most recent call last):
  File "/root/workspace/test3/Test/test.py", line 23, in safe
      entry(*args)    # Catch everything else
        File "/root/workspace/test3/Test/test.py", line 7, in oops
            raise MyError('Spam!')
            MyError: Spam!
            Got <class '__main__.MyError'> Spam!
