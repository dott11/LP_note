#coding=utf-8

# Registering decorated objects to an API
registry = {}
def register(obj): # Both class and func decorator
    registry[obj.__name__] = obj # Add to registry
    return obj # Return obj itself, not a wrapper

@register
def spam(x):
    return(x ** 2) # spam = register(spam)

@register
def ham(x):
    return(x ** 3)

@register
class Eggs: # Eggs = register(Eggs)
    def __init__(self, x):
        self.data = x ** 4
    def __str__(self):
        return str(self.data)
    
print('Registry:')
for name in registry:
    print(name, '=>', registry[name], type(registry[name]))
print('\nManual calls:')
print(spam(2)) # Invoke objects manually
print(ham(2)) # Later calls not intercepted
X = Eggs(2)
print(X)
print('\nRegistry calls:')
for name in registry:
    print(name, '=>', registry[name](3)) # Invoke from registry

Registry:
spam => <function spam at 0x7f5da90c0268> <class 'function'>
ham => <function ham at 0x7f5da90c0620> <class 'function'>
Eggs => <class '__main__.Eggs'> <class 'type'>

Manual calls:
4
8
16

Registry calls:
spam => 9
ham => 27
Eggs => 81

