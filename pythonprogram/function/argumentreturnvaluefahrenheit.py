def convert(f):
	c=(f-32)*5/9
	return c
f=float(input("enter fahrenheit:"))
ans=convert(f)
print("centigrade=",ans)