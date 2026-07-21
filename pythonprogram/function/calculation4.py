def calculation(a,b):
	return a+b,a-b,a*b,a/b
print("Enter any two numbers")
a=int(input())
b=int(input())
s,sb,mul,div = calculation(a,b)
print("addition=",s)
print("subtraction=",sb)
print("multiplication=",mul)
print("division=",div)

