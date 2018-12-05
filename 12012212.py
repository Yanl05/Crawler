def f():
    yield 1
    yield 2
    yield 3
    return 5
g = f()
print(g.__next__())
print(g.__next__())
print(g.__next__())
#print(g.__next__())
