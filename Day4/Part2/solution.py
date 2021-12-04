def check(list):
	a = False
	b = False
	sum1 = 0
	sum2 = 0
	for i in range(5):
		for j in range(5):
			sum1 += list[i][j]
			sum2 += list[j][i]
		if sum1 == -5:
			a = True
			break
		if sum2 == -5:
			b = True
			break
		sum1 = 0
		sum2 = 0
	if (a or b):
		return True
	else:
		return False
	

def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line
file = []
with open('input.txt') as f_in:
	for line in nonblank_lines(f_in):
		file.append(line)

values = file[0].split(',')

arrays = []
for i in range(1, len(file)):
	current = [int(i) for i in file[i].split(' ') if i]
	arrays.append(current)

bingo_chart = {}

c = 0
m = []
for i in range(len(arrays)+1):
	if(i%5 == 0 and i != 0):
		bingo_chart[str(c)] = m
		m = []
		c += 1
	if(i < len(arrays)):
		m.append(arrays[i])

boards = []
flag = 0
for i in range(len(values)):
	a = values[i]
	for j in range(len(bingo_chart)):
			for k in range(5):
				for m in range(5):
					if(str(bingo_chart[str(j)][k][m]) == a):
						bingo_chart[str(j)][k][m] = -1
			if(check(bingo_chart[str(j)])):
				if j not in boards:
					boards.append(j)
				if len(boards) == len(bingo_chart):
					flag = 1
					break
	if(flag == 1):
		break			

sum = 0
for i in range(5):
	for j in range(5):
		if bingo_chart[str(boards[len(boards)-1])][i][j] != -1:
			sum += bingo_chart[str(boards[len(boards)-1])][i][j]

print(sum*int(a))
