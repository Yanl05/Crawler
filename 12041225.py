import mymodule
import imp

mymodule.show()
print(mymodule.name)
#print(dir(mymodule))  # dir   查看模块函数
def show():
    print('*'*20)
#print(mymodule.show())
mymodule.show()
imp.reload(mymodule)
print(show())
# #from mymodule import show  #指定函数
# from mymodule import *  #  * 导入多个
# show()
# dir(mymodule)