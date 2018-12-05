import os

welcome = 'welcome to Heroes world!'
i = 0
while True:
    if os.path.isfile('lock.txt'):
        print('locked')
        break
    username = input('login:')
    password = input('password:')
    i += 1
    if username == 'milo' and password == '123':
        pass
        #break
    else:
        if i == 3:
            open('lock.txt', 'w').write(username)
            break
        continue
    print(welcome)