import random
# 65-90 A-Z  97-122 a-z
for i in range(4):
    a = random.randint(65, 90)
    b = random.randint(97, 122)
    x = [a, b]
    c = random.choice(x)
    print(chr(c), end="")