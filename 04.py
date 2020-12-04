with open('input.txt','r') as f:
	l=[i.split() for i in f.read().split('\n\n')]
z=0
for i in l:
	allow=True
	for j in i:
		if 'cid' in j and len(i)<8:
			allow=False
			break
	else:
		if len(i)<7:
			allow=False
	if not allow:
		break
	for j in i:
		if (('hgt' in j and 'in' in j and not (59<=int(j.split(':')[1].split('in')[0])<=76)) or
			('hgt' in j and 'cm' in j and not (150<=int(j.split(':')[1].split('cm')[0])<=193)) or
			('hgt' in j and not('cm' in j or 'in' in j)) or
			('byr' in j and not (1920<=int(j.split(':')[1])<=2002)) or
			('iyr' in j and not (2010<=int(j.split(':')[1])<=2020)) or
			('eyr' in j and not (2020<=int(j.split(':')[1])<=2030)) or
			('hcl' in j and (not(':#' in j) or len(j.split(':#')[1])!=6 or not (j.split(':#')[1].isalnum() and not any([k in j.split(':#')[1] for k in 'ghijklmnopqrstuvwxyz'])))) or
			('ecl' in j and not ('amb' in j or 'blu' in j or 'brn' in j or 'gry' in j or 'grn' in j or 'hzl' in j or 'oth' in j)) or
			('pid' in j and (len(j.split(':')[1])!=9 or not j.split(':')[1].isdigit()))):
			allow=False
			break
	if allow:
		z+=1
print(z,len(l))