for i in range(10):
    if i == 5:
        print(i*10)
        continue
    if i == 7:
        print(i)
        break
    if i == 2:
        pass
    print(i)

while 1:
    b = input('something:')
    if b == 'no':
        break
a = 1
while a != 'no':
    a = input('something:')
    if a == 'no':
        break