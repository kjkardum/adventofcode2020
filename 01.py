with open('input.txt','r') as f:
	l=[int(i) for i in f.readlines()]
for i,a in enumerate(l):
	for ii,b in enumerate(l[i+1:]):
		for c in l[ii+1:]:
			if a+b+c==2020:
				print(3,a*b*c)