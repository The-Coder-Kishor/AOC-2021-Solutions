file = open('input.txt', 'r')
f1 = file.readlines()
length = len(f1)
c = 0
for i in range(1,length):
  if(int(f1[i]) > int(f1[i-1])):
    c += 1
print(c)
