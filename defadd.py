
class MyList:
    __mylist = []
    def __init__(self, *args):
        self.__mylist = []
        for arg in args:
            self.__mylist.append(arg)
    def __add__(self, x):
        for i in range(0, len(self.__mylist)):
            self.__mylist[i] = self.__mylist[i] + x
        return self.__mylist

    def __sub__(self, x):
        pass

    def __mul__(self, x):
        pass

    def __div__(self, x):
        pass

    def show(self):
        print(self.__mylist)

if __name__ == '__main__':
    l = MyList(1, 2, 3, 4, 5)
    l.show()
    l + 10
    l.show()
