print((lambda l:(sum(1for i in l if i[0][0]<=i[2].count(i[1][0])<=i[0][1]),sum(1for i in l if(i[2][i[0][0]-1]==i[1][0])^(i[2][i[0][1]-1]==i[1][0]))))([[list(map(int,i[0].split('-'))),i[1],i[2]]for i in[i.split()for i in open('input.txt')]]))
