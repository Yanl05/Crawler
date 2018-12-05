import sys

def isType(a):
    try:
        b = float(a)
        return True
    except ValueError as e:
        False

def main():
    while True:
        a = input('请输入数据（数字或字符串）：')
        if isType(a):
            print('输入的是数字')
            c = input('如果要推出请敲1')
            c = int(c)
            if c == 1:
                sys.exit()
        else:
            print('输入的是字符串')
            c = input('如果要推出请敲1')
            c = int(c)
            if c == 1:
                sys.exit()

if __name__ == '__main__':
    main()

#print(isinstance(b, float))
'''if isinstance(a, int):
    print('输入的是数字')
else:
    print('输入的是字符串')
'''