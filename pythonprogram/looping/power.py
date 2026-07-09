print("enter two number")
n1=int(input())
n2=int(input())
p=1
while(n2>0):
	m=0
	i=0
	while(i<n1):
		m=m+p
		i=i+1
	p=m
	n2=n2-1
print("power=",p)