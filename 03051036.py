print(1+1)
print('1' + '1')
class Triangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        Area = self.width * self.height / 2
        return Area


class Square:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        Area = self.width * self.height
        return Area

a = Triangle(5,5)
print(a.getArea())
b = Square(5, 5)
print(b.getArea())   # 多态： 同一个名字 不同的方法
