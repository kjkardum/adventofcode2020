l=list(map(int,open('input.txt').read().split(",")))
def run(l,to=2020):
	d={k:i for i,k in enumerate(l)}
	n=0
	for i in range(len(l),to-1):
		d[n],n=i, i-d.get(n,i)
	return n
print(run(l[:],2020))
print(run(l[:],30000000))