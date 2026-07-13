no=2
s=0
while no<=20:
	d=2
	c=0
	while d<=no//2:
		if no%d==0:
			c=c+1
			break
		d=d+1
	if c==0:
		print(no)
		s=s+no
	no=no+1
print("sum=",s)
