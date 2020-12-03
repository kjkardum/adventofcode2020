with open('input.txt','r') as f:
	l=[[list(map(int,i[0].split('-'))),i[1],i[2]] for i in [i.split() for i in f.readlines()]]
z=0
for i in l:
	 if i[0][0] <= i[2].count(i[1][0]) <= i[0][1]:
	 	z+=1
print('part 1:',z)
z=0
for i in l:
	if (i[2][i[0][0]-1]==i[1][0]) ^ (i[2][i[0][1]-1]==i[1][0]):
		z+=1
print('part 2:',z)