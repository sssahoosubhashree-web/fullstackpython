for num in range(1,1001):
	n=num
	p=0
	dup1=n
	s=0
	dup2=dup1
	while n!=0:
		p=p+1
		n=n//10
	dup1=dup2
	while dup1!=0:
		d=dup1%10
		s=s+d**p
		dup1=dup1//10
	if s==dup2:
		print(dup2)
