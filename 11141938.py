#num = 0
nums = []
for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        nums.append(i)

print([i*10 for i in range(10) if i < 5])
print(sum(nums))
print(sum([i for i in range(10) if i % 3 == 0 or i % 5 == 0]))