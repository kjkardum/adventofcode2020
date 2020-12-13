with open('input.txt','r') as f:
	n=int(f.readline())
	x=f.readline()
	l=[int(i) for i in x.split(",") if i.isnumeric()]
	r=[-i for i,k in enumerate(x.split(",")) if k.isnumeric()]
l2=[]
for i in l:
	l2.append([(n//i+1)*i,i])
print((min(l2)[0]-n)*min(l2)[1])

##NOT MINE CHINESE REMAINDER:
def inv(a, m) : 
    m0 = m 
    x0 = 0
    x1 = 1
    if (m == 1) : 
        return 0
    # Apply extended Euclid Algorithm 
    while (a > 1) : 
        # q is quotient 
        q = a // m
        t = m
        # m is remainder now, process  
        # same as euclid's algo 
        m = a % m 
        a = t
        t = x0
        x0 = x1 - q * x0
        x1 = t
    # Make x1 positive 
    if (x1 < 0) : 
        x1 = x1 + m0
    return x1
# k is size of num[] and rem[].  
# Returns the smallest 
# number x such that: 
# x % num[0] = rem[0], 
# x % num[1] = rem[1], 
# .................. 
# x % num[k-2] = rem[k-1] 
# Assumption: Numbers in num[]  
# are pairwise coprime 
# (gcd for every pair is 1) 
def findMinX(num, rem, k):
    prod = 1
    for i in range(0, k) : 
        prod = prod * num[i]
    result = 0
    for i in range(0,k): 
        pp = prod // num[i] 
        result = result + rem[i] * inv(pp, num[i]) * pp
    return result % prod
num = l
rem = r
k = len(num) 
print(findMinX(num, rem, k)) 
  