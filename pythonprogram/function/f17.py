def facttest(no):
	f=1
	while no>0:
		f=f*no
		no=no-1
	return f
s=facttest(5)+facttest(4)+facttest(3)+facttest(2)+facttest(1)
print("first 5 factorial sum=",s)