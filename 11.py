with open('input.txt','r') as f:
	l=[list(i.strip()) for i in f.readlines()]
t=0
while True:
	l2=[]
	for i,k in enumerate(l):
		l2.append([])
		for j,m in enumerate(k):
			if m=='.':
				l2[-1].append(".")
			if m=='L':
				z=0
				for x in [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]:
					if i+x[0]>=0 and i+x[0]<len(l) and j+x[1]>=0 and j+x[1]<len(l[i+x[0]]):
						if l[i+x[0]][j+x[1]]=='#':
							z+=1
				if not z:
					l2[-1].append("#")
				else:
					l2[-1].append("L")
			if m=='#':
				z=0
				for x in [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]:
					try:
						if i+x[0]>=0 and i+x[0]<len(l) and j+x[1]>=0 and j+x[1]<=len(k):
							if l[i+x[0]][j+x[1]]=='#':
								z+=1
					except:
						pass
				if z>=4:
					l2[-1].append("L")
				else:
					l2[-1].append("#")
	if l!=l2:
		t+=1
		l=[i[:] for i in l2]
	else:
		break
print(t)
z=0
for i in l:
	for j in i:
		if j=='#':
			z+=1
print(z)

with open('input.txt','r') as f:
	l=[list(i.strip()) for i in f.readlines()]
t=0
while True:
	l2=[]
	for i,k in enumerate(l):
		l2.append([])
		for j,m in enumerate(k):
			if m=='.':
				l2[-1].append(".")
			if m=='L':
				z=0
				for x in [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]:
					d=1
					while True:
						try:
							if i+x[0]*d>=0 and i+x[0]*d<len(l) and j+x[1]*d>=0 and j+x[1]*d<len(l[i+x[0]*d]):
								if l[i+x[0]*d][j+x[1]*d]=='#':
									z+=1
									break
								if l[i+x[0]*d][j+x[1]*d]=='L':
									break
							else:
								break
							d+=1
						except:
							break
				if not z:
					l2[-1].append("#")
				else:
					l2[-1].append("L")
			if m=='#':
				z=0
				for x in [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]:
					d=1
					while True:
						try:
							if i+x[0]*d>=0 and i+x[0]*d<len(l) and j+x[1]*d>=0 and j+x[1]*d<len(l[i+x[0]*d]):
								if l[i+x[0]*d][j+x[1]*d]=='#':
									z+=1
									break
								if l[i+x[0]*d][j+x[1]*d]=='L':
									break
							else:
								break
							d+=1
						except:
							break
				if z>=5:
					l2[-1].append("L")
				else:
					l2[-1].append("#")
	if l!=l2:
		t+=1
		l=[i[:] for i in l2]
	else:
		break
print()
print(t)
z=0
for i in l:
	for j in i:
		if j=='#':
			z+=1
print(z)