with open('input.txt','r') as f:
	l=[i.split() for i in f.read().split('\n\n')]
z=0
for i in l:
	for j in set("".join(i)):
		if "".join(i).count(j)==len(i):
			z+=1
print(z)