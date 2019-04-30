#coding=utf-8

class Person:
    def __init__(self, name): # On [Person()]
        self._name = name # Triggers __setattr__!
    def __getattr__(self, attr): # On [obj.undefined]
        print("__getattr__")
        if attr == 'name': # Intercept name: not stored
            print('fetch...')
            return self._name # Does not loop: real attr
        else: # Others are errors
            raise AttributeError(attr)
    def __setattr__(self, attr, value): # On [obj.any = value]
        print("__setattr__")
        if attr == 'name':
            print('change...')
            attr = '_name' # Set internal name
        self.__dict__[attr] = value # Avoid looping here
    def __delattr__(self, attr): # On [del obj.any]
        print("__delattr__")
        if attr == 'name':
            print('remove...')
            attr = '_name' # Avoid looping here too
        del self.__dict__[attr] # but much less common

bob = Person('Bob Smith') # bob has a managed attribute
bob.sex="male"
print(bob.sex)
print(bob._name)
print(bob.__dict__)
print(bob.name) # Runs __getattr__
bob.name = 'Robert Smith' # Runs __setattr__
print(bob.name)
del bob.name # Runs __delattr__
print('-'*20)
sue = Person('Sue Jones') # sue inherits property too
print(sue.name)
# print(Person.name.__doc__) # No equivalent here

__setattr__
__setattr__
male
Bob Smith
{'_name': 'Bob Smith', 'sex': 'male'}
__getattr__
fetch...
Bob Smith
__setattr__
change...
__getattr__
fetch...
Robert Smith
__delattr__
remove...
--------------------
__setattr__
__getattr__
fetch...
Sue Jones

