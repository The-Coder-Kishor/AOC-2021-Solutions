with open('input.txt',"r") as f:
	file = [l.strip() for l in f.readlines()]


def max(list):
	value_1 = 0
	for line in list: 
		if line[pos] == "1": 
			value_1 += 1
	if value_1 >= len(list)-value_1:
		return "1"
	return "0"

o2_rating,co2_rating = file.copy(),file.copy()
pos = 0

while len(o2_rating) > 1: 
	most_common = max(o2_rating) 
	for line in o2_rating[:]:
		if line[pos] != most_common: 
			o2_rating.pop(o2_rating.index(line)) 
	pos += 1 
	

pos = 0

while len(co2_rating) > 1:
	most_common = max(co2_rating)
	for line in co2_rating[:]:
		if line[pos] == most_common:
			co2_rating.pop(co2_rating.index(line))
	pos += 1

life_support = int(o2_rating[0],2) * int(co2_rating[0],2)
print(life_support)
