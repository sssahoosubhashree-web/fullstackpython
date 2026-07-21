def rectangle():
	l=float(input("enter length: "))
	b=float(input("enter breadth: "))
	area=l*b
	per=2*(l+b)
	return area,per
a,p=rectangle()
print("area=", a)
print("perimeter", p)
