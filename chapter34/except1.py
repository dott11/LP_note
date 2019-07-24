#coding=utf-8

class MyBad(Exception):pass

try:
    raise MyBad('Sorry--my mistakes!')
except MyBad as X:
    print(X)
    print(X.args)
    print(X.__class__.__base__.__base__.__base__)

Sorry--my mistakes!
('Sorry--my mistakes!',)
<class 'object'>
