l=[int(i) for i in open("input.txt")]
for i in range(25,len(l)):
	for j in range(i-25,i-1):
		for k in range(j+1,i):
			if l[j]+l[k]==l[i]:
				break
		if l[j]+l[k]==l[i]:
			break
	if not l[j]+l[k]==l[i]:
		v=l[i]
		break
print(l[i])
sums=[l[0]]
for i in l[1:]:
	sums.append(sums[-1]+i)
for i in range(len(l)):
	for j in range(i+1,len(l)):
		if sums[j]-sums[i]==v:
			print(max(l[517:534])+min(l[517:534]))
			break
	if j<len(l)-1:
		break