with open('input.txt','r') as f:
	l=[("("+i+")").strip().replace("(","( ").replace(")"," )").split() for i in f.readlines()]

total=0
for i in l:
	t=[]
	d=[t]
	for j,k in enumerate(i):
		if k=="(":
			d[-1].append([])
			d.append(d[-1][-1])
		elif k==")":
			z=0
			op="+"
			for h in d[-1]:
				if h in "+*":
					op=h
				else:
					if op=="+":
						z+=int(h)
					else:
						z*=int(h)
			d.pop(len(d)-1)
			d[-1][-1]=str(z)
		else:
			d[-1].append(k)
	total+=int(t[-1])
print(total)


print(sum(eval(i)for i in["("+i.replace("*",")*(")+")"for i in open("input.txt")]))