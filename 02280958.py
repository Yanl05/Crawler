#闭包
# 闭包函数必须要有内嵌函数
# 内嵌函数需要引用该嵌套函数上一级变量
# 闭包函数必须返回内嵌函数
def hello_conf(prefix):
    def hello(name):
        print(prefix, name)
    return hello

a = hello_conf('Good Morning!')
print(a.__name__)
print(id(a))
a('milo')
a('jack ma')

b = hello_conf('Good Afternoon!')
print(b.__name__)
print(id(b))
b('milo')
b('jack ma')
