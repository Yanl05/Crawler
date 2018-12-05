#装饰器
import time
def deco(func):
    def wrappere():
        startT = time.time()
        func()
        endT = time.time()
        msecs = (endT - startT) * 1000
        print("it's %f ms" % msecs)
    return wrappere
@deco  #装饰器
def myfunc():
    print('myfunc start...')
    time.sleep(2)
    print('myfunc end...')

#myfunc = deco(myfunc)
myfunc()