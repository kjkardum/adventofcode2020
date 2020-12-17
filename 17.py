from copy import deepcopy as copy

l=[list("."*6)+list(i.strip())+list("."*6) for i in open('input.txt')]
lt=[list("."*len(l[0]))]*6+[list("."*(13+len(l)))for i in l]+[list("."*len(l[0]))]*6
l=[list("."*len(l[0]))]*6+l+[list("."*len(l[0]))]*6
l=[copy(lt)]*6+[l]*1+[copy(lt)]*6
moves=[[i,j,k] for i in [-1,0,1] for j in [-1,0,1] for k in [-1,0,1] if [i,j,k]!=[0,0,0]]
for t in range(6):
	l2=[]
	for i,k in enumerate(l):
		l2.append([])
		for ii,kk in enumerate(k):
			l2[-1].append([])#j,m
			for iii,kkk in enumerate(kk):
				if kkk=='#':
					z=0
					for x in moves:
						if 0<=i+x[0]<len(l) and 0<=ii+x[1]<len(l[i+x[0]]) and 0<=iii+x[2]<len(l[i+x[0]][ii+x[1]]):
							if l[i+x[0]][ii+x[1]][iii+x[2]]=='#':
								z+=1
					if z==2 or z==3:
						l2[-1][-1].append("#")
					else:
						l2[-1][-1].append(".")
				if kkk=='.':
					z=0
					for x in moves:
						if 0<=i+x[0]<len(l) and 0<=ii+x[1]<len(l[i+x[0]]) and 0<=iii+x[2]<len(l[i+x[0]][ii+x[1]]):
							if l[i+x[0]][ii+x[1]][iii+x[2]]=='#':
								z+=1
					if z==3:
						l2[-1][-1].append("#")
					else:
						l2[-1][-1].append(".")
	l=copy(l2)
print(sum(sum(j.count('#')for j in i) for i in l))
############
l=[list("."*6)+list(i.strip())+list("."*6) for i in open('input.txt')]
lt=[list("."*len(l[0]))]*6+[list("."*((2*6)+len(l)))for i in l]+[list("."*len(l[0]))]*6
l=[list("."*len(l[0]))]*6+l+[list("."*len(l[0]))]*6
l=[copy(lt)]*6+[l]*1+[copy(lt)]*6
ltt=[copy(lt)]*(2*6+1)
l=[copy(ltt)]*6+[l]*1+[copy(ltt)]*6
moves=[[i,j,k,h] for i in [-1,0,1] for j in [-1,0,1] for k in [-1,0,1] for h in [-1,0,1] if [i,j,k,h]!=[0,0,0,0]]
for t in range(6):
	l2=[]
	for i,k in enumerate(l):
		l2.append([])
		for ii,kk in enumerate(k):
			l2[-1].append([])#j,m
			for iii,kkk in enumerate(kk):
				l2[-1][-1].append([])
				for iiii,kkkk in enumerate(kkk):
					if kkkk=='#':
						z=0
						for x in moves:
							if 0<=i+x[0]<len(l) and 0<=ii+x[1]<len(l[i+x[0]]) and 0<=iii+x[2]<len(l[i+x[0]][ii+x[1]]) and 0<=iiii+x[3]<len(l[i+x[0]][ii+x[1]][iii+x[2]]):
								if l[i+x[0]][ii+x[1]][iii+x[2]][iiii+x[3]]=='#':
									z+=1
						if z==2 or z==3:
							l2[-1][-1][-1].append("#")
						else:
							l2[-1][-1][-1].append(".")
					if kkkk=='.':
						z=0
						for x in moves:
							if 0<=i+x[0]<len(l) and 0<=ii+x[1]<len(l[i+x[0]]) and 0<=iii+x[2]<len(l[i+x[0]][ii+x[1]]) and 0<=iiii+x[3]<len(l[i+x[0]][ii+x[1]][iii+x[2]]):
								if l[i+x[0]][ii+x[1]][iii+x[2]][iiii+x[3]]=='#':
									z+=1
						if z==3:
							l2[-1][-1][-1].append("#")
						else:
							l2[-1][-1][-1].append(".")
	l=copy(l2)
print(sum(sum(sum(k.count('#') for k in j)for j in i) for i in l))