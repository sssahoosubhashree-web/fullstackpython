print("enter basic salary")
sal=(float(input()))
da,hra=0,0
if sal >=5000:
	da=sal*30/100
	hra=sal*20/100
total=sal+da+hra

print("basic salary =",sal)
print("DA =",da)
print("HRA =",hra)
print("TOTAL SALARY=",total)
