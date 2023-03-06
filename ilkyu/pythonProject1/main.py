sum = 0
a = 357
for i in range(6):
    sum += a + a * i
    print(i + 1, ':', a + a * i)

print('sum : ', sum)
