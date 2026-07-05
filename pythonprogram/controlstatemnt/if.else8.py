print("enter a salary")
sal=float(input())
if sal>=5000:
	da=sal*30/100
	hra=sal*20/100
else:
	da=sal*10/100
	hra=sal*15/100
total=sal+da+hra
print("basic salary=",sal)
print("da=",da)
print("hra=",hra)
print("total salary=",total)
