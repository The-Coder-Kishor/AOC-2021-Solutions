import sys
file = open('input.txt', 'r')
reading = file.readline().split(',')
positions = []
min = int(reading[0])
max = 0
for i in range(len(reading)):
    if int(reading[i]) > max:
        max = int(reading[i])   
    if int(reading[i]) < min:
        min = int(reading[i])
    positions.append(int(reading[i]))
sum = sys.maxsize
for i in range(min, max+1):
    curr_sum = 0
    for j in range(len(positions)):
        dist = abs(positions[j] - i)
        curr_sum += (dist * (dist+1)/2)
    if (sum > curr_sum):
        sum = curr_sum
print(sum)
