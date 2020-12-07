with open('input.txt','r') as f:
	l= [i.strip().split('contain ') for i in f.readlines()]
d={}
d2={}
z=[]
for i in range(len(l)):
	l[i][0]=l[i][0].replace('bags','').strip()
	if 'no other bags' in l[i][1]:
		continue
	l[i][1]=l[i][1].replace(' bags','').replace(' bag','').replace('.','').split(', ')
	if l[i][0] not in d:
		d[l[i][0]]=[]
	for j in l[i][1]:
		x=j.split(" ")
		d[l[i][0]].append([int(x[0])," ".join(x[1:])])
		if " ".join(x[1:]) not in d2:
			d2[" ".join(x[1:])]=[]
		d2[" ".join(x[1:])].append(l[i][0])
def bags(n,steps):
	if n in d2:
		for i in d2[n]:
			if i not in steps:
				bags(i,steps+[i])
	z.append(steps)
bags('shiny gold',[])
sets=set()
for i in z:
	for j in i:
		sets.add(j)
print(len(sets),sep="\n")

def bags2(n,steps):
	z=0
	if n in d:
		for i in d[n]:
			if i[1] not in steps:
				z+=i[0]+i[0]*bags2(i[1],steps+[i[1]])
	return z
z=bags2('shiny gold',[])
print(z,sep='\n')