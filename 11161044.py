# fileobject = open(filename, mode)
# r 只读
# w 写入，重建文件
# a 写入，在文末尾追加，如果不存在文件，则创建
# + 更新
# b 打开二进制文件
# U支持所有换行符
f = open('lock.txt', 'r')
#print(f.read())
#print(f.readline())
#print(f.readlines(2))
print(f.read(4))
f.close()
f = open('abc', 'w')
print(f.write('abcdef'))
f = open('abc', 'r')
print(f.read())
f.close()
f = open('abc', 'a')
f.write('yanl')
f = open('abc', 'r')
print(f.read())
f.close()
f = open('abc', 'w+')
print(f.read())
f.write('666')
print(f.read())
f.close()
f = open('abc', 'a+')
print(f.read())
f.close()
f = open('abc', 'r+')
print(f.read())
f.write('xyz')
f.flush()   #提交更新
f.close()
f = open('abc', 'rb')
#print(f.read())
#seek（偏移量，选项）
#                       选项为0 指向头部
#                       选项为1 从当前位置向后移动偏移量
#                       选项为2 从尾部 向前移动偏移量
f.seek(-2, 2)
print(f.read())


