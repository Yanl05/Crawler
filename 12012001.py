def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
g = fib(10)
for i in range(10):

    print(g.__next__())