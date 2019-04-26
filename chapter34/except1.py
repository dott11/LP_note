#coding=utf-8

class MyBad(Exception):pass

try:
    raise MyBad('Sorry--my mistakes!')
except MyBad as X:
    print(X)
    print(X.args)