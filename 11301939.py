def f2(x):
    if x < 0:
        return -x
    else:
        return x
x = input("请输入一个数字：")
x = int(x)
#a = f2(x)
print('%s' % f2(x))