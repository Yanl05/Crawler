map = ((0, 0), (1, 0), (2, 0)
       , (0, 1), (1, 1), (2, 1)
       , (0, 2), (1, 2), (2, 2))
player1 = ['milo', 100]
print(player1[0], player1[1])
player1d = {'name': 'milo', 'HP': 100} #字典， 通过键来定位，不是通过偏移量 key:value
d = {1: 'a', 2: 'b'}
d[3] = 'c' #向字典中添加

for k in d:
    print(d[k])
print('name' in player1d)
print(d)
print(player1d['name'])
d[3] = 'gg'
print(d)
del d[3]    #删除字典中的key
print(d)
print(d.items())
print(d.pop(2)) #删除并返回
d.clear()  #清除整个字典
print(d)
