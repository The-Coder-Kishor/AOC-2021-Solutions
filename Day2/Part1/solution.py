file = open('input.txt', 'r')
f1 = file.readlines()
length = len(f1)
horizontal = 0
depth = 0
for i in range(length):
    x = f1[i].split(' ')
    if x[0] == 'forward':
        horizontal += int(x[1])
    elif x[0] == 'up':
        depth -= int(x[1])
    else:
        depth += int(x[1])

value = horizontal * depth
print(value)
