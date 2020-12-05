with open('input.txt','r') as f:
	l=[i.strip().replace('F','0').replace('B','1').replace('L','0').replace('R','1') for i in f.readlines()]
l=[int(i[:7],2)*8+int(i[7:],2) for i in l]
print(1,max(l))
l.sort()
for i in range(1,len(l)):
	if l[i]-l[i-1]==2:
		print(2,l[i]-1)