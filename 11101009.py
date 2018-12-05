player1 = "milo 100 50"
milo = "100 60 0"
zou = "100 100 100"
player1 = ['milo', 100, 50]
milo = [100, 60, 0, 50, 60]
list1 = [1]
print(type(list1))
print(milo[1])
print(milo[1:4:2])
print(milo + list1)
for i in milo:
    print(i)
player2 = 'milo 90 60'
print(player1)
print(id(player1))
player1[1] = 90
print(player1)
print(id(player1))
player1.append(10)
print(player1)
player1.insert(1, 'man')
print(player1)