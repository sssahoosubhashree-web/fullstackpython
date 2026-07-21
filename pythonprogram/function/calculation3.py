def calculation():
	a=int(input("enter first number:"))
	b=int(input("enter second number"))
	return a+b,a-b,a*b,a/b
s,sb,m,d=calculation()
print("addition=",s)
print("subtraction=",sb)
print("multiplication=",m)
print("division=",d)
