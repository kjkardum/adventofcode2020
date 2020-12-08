with open('input.txt','r') as f:
	l=[i.split() for i in f.readlines()]
def tr(l):
	i,z,l2=0,0,[0]*len(l)
	while True:
		if i>=len(l) or l2[i]:
			break
		l2[i]+=1
		if l[i][0]=='jmp':
			i+=int(l[i][1])-1
		if l[i][0]=='acc':
			z+=int(l[i][1])
		i+=1
	return(z,i>=len(l))
for i in range(len(l)):
	op={'nop':'jmp','jmp':'nop','acc':''}[l[i][0]]
	if op:
		z,k=tr(l[:i]+[[op,l[i][1]]]+l[i+1:])
		if k:
			print(z)