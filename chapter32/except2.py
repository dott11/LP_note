#coding=utf-8

try:
    raise IndexError
#     print("try no except")
except IndexError:
    print("got exception")
else:
    print("else")
finally:
    print("finally")
print("out of try")

got exception
finally
out of try
