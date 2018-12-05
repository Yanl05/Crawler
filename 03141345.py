try:
    s = 'hello'
    print(s[10])
except Exception as e:  # 有异常执行下面代码
    print(repr(e))
else:   # 无异常执行下面代码
    print('无异常')

try:
    f = open('defadd.py', 'r')
    fr = f.read()
    print(fr)
finally:    # 上面无异常也执行
    f.close()

# with ... as
with open('defadd.py', 'r') as f: # 对象消亡的时候自动调用close
    f.read()

# 抛出异常 raise
# if 1:
#     raise NameError('your name error')

# assert

l = []
assert len(l), '长度'