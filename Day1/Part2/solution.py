file = open('input.txt', 'r')
f1 = file.readlines()
length = len(f1)
c = 0
start = 0
sum = int(f1[0]) + int(f1[1]) + int(f1[2])
for i in range(3, length):
    newsum = int(f1[i]) + sum - int(f1[start])
    if newsum > sum:
       c += 1
    sum = newsum
    start += 1
print(c)
