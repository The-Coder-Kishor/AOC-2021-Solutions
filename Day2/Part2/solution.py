file = open('input.txt', 'r')
f1 = file.readlines()
length = len(f1)
horizontal = 0
depth = 0
aim = 0
for i in range(length):
    x = f1[i].split(' ')
    if x[0] == 'forward':
        horizontal += int(x[1])
        depth += (int(x[1]) * aim)
    elif x[0] == 'up':
        aim -= int(x[1])
    else:
        aim += int(x[1])

value = horizontal * depth
print(value)
