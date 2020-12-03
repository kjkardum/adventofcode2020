with open('input.txt','r') as f:
	l=[list(i.replace('\n','')) for i in f.readlines()]
n=len(l[0])
total=1
for st in [[1,1],[3,1],[5,1],[7,1],[1,2]]:
	t,k,i=0,0,0
	while i<len(l):
		if l[i][k]=='#':
			t+=1
		k=(k+st[0])%n
		i+=st[1]
	total*=t
print('total',total)