with open('input.txt','r') as f:
	l=[i.split("\n")[:-1] for i in f.read().split('mask = ')][1:]
def set_bit(n, p, b):
  return(n&~(1<<p))|((b<<p)&(1<<p)) 

p={}
for i,*m in l:
	bits={}
	for ii,j in enumerate(i):
		if j!='X':
			bits[35-ii]=int(j)
	for k in m:
		loc,val=map(str, k.split(' = '))
		loc=int(loc[4:-1])
		val=int(val)
		for j in bits:
			val=set_bit(val,j,bits[j])
		p[loc]=val
print(sum(p.values()))

p={}
for i,*m in l:
	bits={}
	bits2=[]
	for ii,j in enumerate(i):
		if j=="1":
			bits[35-ii]=1
		elif j=="X":
			bits2.append(35-ii)
	for k in m:
		loc,val=map(str, k.split(' = '))
		loc=int(loc[4:-1])
		val=int(val)
		for j in bits:
			if bits[j]:
				loc=set_bit(loc,j,bits[j])
		for b in range(2**len(bits2)):
			loc2=loc
			b=bin(b)[2:].zfill(len(bits2))
			bits3={k:int(b[i]) for i,k in enumerate(bits2)}
			for j in bits3:
				loc2=set_bit(loc2,j,bits3[j])
			p[loc2]=val
print(sum(p.values()))
