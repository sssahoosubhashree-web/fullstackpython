def sical():
	print("enter principal")
	p=float(input())
	print("enter rate")
	r=float(input())
	print("enter time")
	t=float(input())
	si=p*r*t/100
	return si
ans=sical()
print("simple interest=",ans)

