'''
Heroes beta-0.2
milo  str map if while
2017-08-20
'''
'''
welcome = 'welcome to Heroes world!'
mapmsg = '#######'
mapins = "\n-*- the world is like this -*-\n %s \n the '*' is you " % (mapmsg,)
map = ['#','#','#','#','#','#','#']
instruction = '''
'''
contrl your hero:
| 'a'for left | 'd' for right |'''
'''
print(welcome)

name = input('input your name:')
hp = 100

if not name:
    name = 'player01'

usermsg = {'name':name,'hp':hp}

print("your hero's name is:",usermsg['name'],'Hp is :',usermsg['hp'])
print(mapins,instruction)

point = 0
while 1:
    map[point] = "*"
    print('you are here',"".join(map))
    userinput = input('go or quit:')

    if userinput == 'd' and point < 6:
        map[point] = '#'
        point +=1
    elif userinput == 'a' and point > 0:
        map[point] = '#'
        point -=1
    elif userinput == 'quit':
        print("goodbey!!")
        break
    else:
        print(instruction)
'''
import random

welcome = 'welcome to Heroes world!'
mapmsg = '#######'
mapins = "-*- the world is like this -*-\n %s \n this '*' is you \n" % (mapmsg, )
map = ['#', '#', '#', '#', '#', '#', '#']
instruction = '''
contrl your hero:
'a' for left ,'d' for right
'''
print(welcome)
name = input('input your name:')
hp = 100
if not name:
    name = 'player1'
usermsg = {'name': name, 'HP': hp}
print("your hero's is :", usermsg['name'], "HP is :", usermsg['HP'])
print(mapins, instruction)

def apple(hp):
     hp += 10
     return hp

def bomb(hp):
    hp -= 10
    return hp

eventlist = [apple, bomb]

point = 0   #初始坐标

while 1:
    map[point] = '*'
    print('you are here', "".join(map))  #join  连接成字符串
    userinput = input('go or quit')

    if userinput == 'd' and point < 6:
        map[point] = '#'
        point += 1
        usermsg['HP'] = random.choice(eventlist)(usermsg['HP'])
        print('blood is %s' % usermsg['HP'])
    elif userinput == 'a' and point > 0:
        map[point] = '#'
        point -= 1
        usermsg['HP'] = random.choice(eventlist)(usermsg['HP'])
        print('blood is %s' % usermsg['HP'])
    elif userinput == 'quit':
        print('bye  GG')
        break
    else:
        print(instruction)

    # if point == 3:
    #     usermsg['HP'] = apple(usermsg['HP'])
    #     print('blood is %s' % usermsg['HP'])
    #
    # if point == 4:
    #     usermsg['HP'] = bomb(usermsg['HP'])
    #     print('blood is %s' % usermsg['HP'])
# def  定义函数  第一个单词小写 第二个单词开始大写
#