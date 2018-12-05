a = 99
def f():
    global a
    a = 10
    print(a)
f()
print('%d' % a)

def machine(x = '5', y = '奶油'):
    print('制作一个 %d 元的 %s 味道的冰激凌' % (x, y))

l = [5, '巧克力']

print(machine(*l))

d = {'x': 5, 'y': '薄荷'}
print(machine(**d))
