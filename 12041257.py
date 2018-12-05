#from mymodule import show  #指定函数
from mymodule import *  #  * 导入多个
import imp
show()
def show():
    print('#' * 20)
show()
#imp.reload(mymodule)
show()