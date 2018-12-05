class Human:
    '''
        This is Human class!
    '''
    name = 'ren'
    gender = 'male'
    age = '25'
    __money = 8000

    def __init__(self, name, age):
        print('#'*50)
        self.name = name
        self.age = age
        print('#' * 50)

    def __str__(self):
        msg = 'hi ! i am the object of Human!'
        return msg  # 直接打印对象 会自动调用

    def say(self):
        print('my name is %s ,I have %d' % (self.name, self.__money))
        self.__lie()

    def __lie(self):
        print('I have 5000')



zhangsan = Human('zhangsan', '25')
print(zhangsan.name, zhangsan.age)
print(zhangsan.say())
print(Human.name)
print(zhangsan)  # 直接打印对象会输出  __str__
print(Human.__doc__)   # __doc__  可以看到注释