with open('input.txt','r') as f:
	l=sorted([int(i) for i in f.readlines()])
l,z1,z3,di=[0]+l+[l[-1]+3],0,0,{}
for i in range(1,len(l)):
	if l[i]-l[i-1]==1:
		z1+=1
	if l[i]-l[i-1]==3:
		z3+=1
def d(i=0):
	if l[i]==l[-1]:
		return 1
	z=0
	if i in di:
		return di[i]
	for j in range(i+1,min(len(l),i+4)):
		if 0<l[j]-l[i]<4:
			z+=d(j)
	di.update({i:z})
	return z
print(z1*z3,d())