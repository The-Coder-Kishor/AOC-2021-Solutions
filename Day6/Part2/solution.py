file = open('input.txt', 'r')
ages_str = file.readline().split(',')
ages = []
for i in range(9):
    ages.append(0)
for i in ages_str:
    ages[int(i)] = ages[int(i)] + 1
for i in range(256):
    temp = ages[0]
    ages[0] = ages[1]
    ages[1] = ages[2]
    ages[2] = ages[3]
    ages[3] = ages[4]
    ages[4] = ages[5]
    ages[5] = ages[6]
    ages[6] = ages[7] + temp
    ages[7] = ages[8]
    ages[8] = temp
print("after one day")
for i in range(9):
    print(ages[i])
sum = 0
for i in range(9):
    sum = sum + ages[i]
print(sum)
