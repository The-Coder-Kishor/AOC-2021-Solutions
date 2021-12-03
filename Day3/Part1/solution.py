file = open('input.txt', 'r')
f1 = file.readlines()
length1 = len(f1)
length2 = len(f1[0])
value1 = []
value0 = []
gammarate = []
epsilonrate = []

for i in range(length2-1):
    value1.append(0)
    value0.append(0)

for i in range(length1):
    for j in range(length2-1):
        if f1[i][j] == '0':
            value0[j] = value0[j] + 1
        else:
            value1[j] = value1[j] + 1

for i in range(length2-1):
    if value0[i] >= value1[i]:
        gammarate.append(0)
        epsilonrate.append(1)
    else:
        gammarate.append(1)
        epsilonrate.append(0)

gamma = 0
epsilon = 0
for i in range(length2-1):
    gamma = gamma + gammarate[i]*(2**(length2-i-2))
    epsilon = epsilon + epsilonrate[i]*(2**(length2-i-2))


print(gamma*epsilon)
