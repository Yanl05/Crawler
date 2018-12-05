x = int(input('first:'))
o = input('operator:')
y = int(input('second:'))

operator = {
            '+': x + y,
            '-': x - y,
            '*': x * y,
            '/': x / y}
result = operator.get(o, 'please input +|-|*|/')
print(result)
'''
if o == '+':
    print(x + y)
elif o == '-':
    print(x - y)
elif o == '*':
    print(x * y)
elif o == '/':
    print(x / y)
else:
    pass
'''