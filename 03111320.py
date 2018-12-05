class Father:
    money = 1000000
    __money = 2000000

    def driver(self):
        print('I can driver a car!')

class Mother:
    mm = 10000

class Son(Father, Mother):    # 继承  只能继承公有属性和公有方法 ,可以继承多个类，不同类中方法同名，只能继承第一个
    def driver(self):
        print('i can drive tank!')  # 重载 继承父类的方法 重新写一下
        Father.driver(self)
    def pay(self):
        print(self.money)

tom = Father()
print(tom.money)
tom.driver()   # 有return的 要print才能输出，定义里有print的直接打名字

print('#' * 50)

jerry = Son()
print(jerry.money)
jerry.driver()
jerry.pay()

