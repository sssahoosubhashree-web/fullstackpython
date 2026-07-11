for n in range(1,10000):
	i=1
	s=0
	while(i<n):
		if(n%i==0):
			s=s+i
		i=i+1
	if(s==n):
		print(n,"perfectnumber")