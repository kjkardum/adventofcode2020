with open('input.txt','r') as f:
	l=[i.split() for i in f.readlines()]
l=[[i[0].split('-'),i[1].replace(":",""),i[2]] for i in l]
z=0
for i in l:
	 if i[2].count(i[1])>=int(i[0][0]) and i[2].count(i[1])<=int(i[0][1]):
	 	z+=1
print('part1',z)
z=0
for i in l:
	if (i[2][int(i[0][0])-1]==i[1] and not i[2][int(i[0][1])-1]==i[1]) or (not i[2][int(i[0][0])-1]==i[1] and i[2][int(i[0][1])-1]==i[1]):
		z+=1
print('part2',z)