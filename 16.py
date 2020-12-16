with open('input.txt','r') as f:
	r=f.read().split('\n\n')
	c=[i.split(": ") for i in r[0].split('\n')]
	c=[[i[0]]+i[1].split(" or ") for i in c]
	c=[[i[0]]+[list(map(int,j.split("-"))) for j in i[1:]] for i in c]
	c=[[i[0]]+[range(j[0],j[1]+1) for j in i[1:]] for i in c]
	my=[list(map(int,i.split(","))) for i in r[1].split('\n')[1:]][0]
	l=[list(map(int,i.split(","))) for i in r[2].split("\n")[1:]]

#print(c)
#print(my)
#print(l)

l2,z=[],0
for i in l:
	valid=True
	for polje in i:
		for r in c:
			if polje in r[1] or polje in r[2]:
				break
		else:
			valid=False
			z+=polje
	if valid:
		l2.append(i)
print(z)

cn={}
def perm(i,p):
	if i>=len(c):
		return p
	for j,r in enumerate(c):
		if i in cn.get(r[0],[]):
			continue
		if r[0] not in p:
			for ii in l2:
				if ii[i] not in r[1] and ii[i] not in r[2]:
					cn[r[0]]=cn.get(r[0],[])+[i]
					break
			else:
				x=perm(i+1,p+[r[0]]) 
				if x:
					return x
z=1
for i,k in enumerate(perm(0,[])):
	if 'departure' in k:
		z*=my[i]
print(z)