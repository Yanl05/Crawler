from functools import reduce
def myadd(x, y):
    return x + y
sum = reduce(myadd, (1, 2, 3))
print(sum)

sum = reduce(lambda x, y: x + y, (1, 2, 3, 4))
print(sum)