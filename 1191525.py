sum = 0
for i in range(101): # 不能直接用100 进行迭代  需要加range（）
    sum = sum + i
print(sum)

sum = 0
for i in range(101):
    if i % 3 == 0:
        sum = sum + i
    if i % 5 == 0:
        sum = sum + i
print(sum)