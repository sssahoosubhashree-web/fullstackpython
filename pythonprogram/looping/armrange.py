for n in range(1,10000,1):

	p=0
	s=0
	dup1=n
	while(dup1!=0):
		p=p+1
		dup1=dup1//10
	dup1=n
	while(dup1!=0):
		d=dup1%10
		s=s+d**p
		dup1=dup1//10
	if(s==n):
		print(n,"armstrong number")
	