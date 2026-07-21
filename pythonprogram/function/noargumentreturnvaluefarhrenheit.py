def convert():
	f=float(input("enter fahrenheit"))
	c=(f-32)*5/9
	return c
ans=convert()
print("centigrade=",ans)