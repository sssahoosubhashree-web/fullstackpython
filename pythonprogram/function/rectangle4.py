def rectangle(l,b):
	area=l*b
	per=2*(l+b)
	return area,per
length=float(input("enter length: "))
breadth=float(input("enter breadth: "))
a,p=rectangle(length,breadth)
print("area=", a)
print("perimeter=", p)