#coding=utf-8

class MyList():
    def __init__(self, start):
        #self.wrapped = start[:] # Copy start: no side effects
        self.wrapped = [] # Make sure it's a list here
        for x in start: self.wrapped.append(x)
    def __add__(self, other):
        return MyList(self.wrapped + other)
    def __mul__(self, time):
        return MyList(self.wrapped * time)
    def __getitem__(self, offset):
        return self.wrapped[offset]
    def __len__(self):
        return len(self.wrapped)
    def __getslice__(self, low, high):
        return MyList(self.wrapped[low:high])
    def append(self, node):
        self.wrapped.append(node)
    def __getattr__(self, name): # Other methods: sort/reverse/etc
        return getattr(self.wrapped, name)
    def __repr__(self):
        return repr(self.wrapped)

class MyListSub(MyList):
    calls = 0 # Shared by instances
    def __init__(self, start):
        self.adds = 0 # Varies in each instance
        MyList.__init__(self, start)
    def __add__(self, other):
        MyListSub.calls += 1 # Class-wide counter
        self.adds += 1 # Per-instance counts
        return MyList.__add__(self, other)
    def stats(self):
        return self.calls, self.adds # All adds, my adds

if __name__ == '__main__':
    x = MyListSub('spam')
    y = MyListSub('foo')
    print(x[2])
    print(x[1:])
    print(x + ['eggs'])
    print(x + ['toast'])
    print(y + ['bar'])
    print(x.stats())
    print(y.stats())

a
['p', 'a', 'm']
['s', 'p', 'a', 'm', 'eggs']
['s', 'p', 'a', 'm', 'toast']
['f', 'o', 'o', 'bar']
(3, 2)
(3, 1)
