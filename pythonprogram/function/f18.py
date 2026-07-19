def facttest(no):
	f=1
	while no>0:
		f=f*no
		no=no-1
	return f
print("enter a number")
res=facttest(int(input()))
print("factorial=",res)