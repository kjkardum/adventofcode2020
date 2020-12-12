l=[[i[0],int(i[1:])] for i in open('input.txt')]
d={'N':-1j,'S':1j,'E':1,'W':-1}
c,z=1+0j,0j
for i in l:
	if i[0]=='F':
		z+=c*i[1]
	elif i[0]in'LR':
		c=c*1j**(i[1]//90*(1if'R'==i[0] else-1))
	else:
		z+=d[i[0]]*i[1]
print(int(abs(z.real)+abs(z.imag)))

z,w=0j,10-1j
for i in l:
	if i[0]=='F':
		z+=w*i[1]
	elif i[0]in'LR':
		w=w*1j**(i[1]//90*(1if'R'==i[0] else-1))
	else:
		w+=d[i[0]]*i[1]
print(int(abs(z.real)+abs(z.imag)))