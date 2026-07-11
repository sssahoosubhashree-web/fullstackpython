for n in range(1,11,1):
	temp=n
	s=0
	while (temp!=0):
		r=temp%10
		m=1
		for i in range (1,r+1):
			m=m*i
		s=s+m
		temp=temp//10
	if (n==s):
		print ("Strong number =", s)
