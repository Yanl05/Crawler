x = 1
y = 2
# x = int(x)
# y = int(y)
print('fibonacci数列第 %s 位 %s' % (x, x))
print('fibonacci数列第 %s 位 %s' % (y, y))
for i in range(3, 11):
    sum = x + y
    sum = int(sum)
    print('fibonacci数列第 %d 位 %d' % (i, sum))
    x = y
    y = sum