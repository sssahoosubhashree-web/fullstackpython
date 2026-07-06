print("enter a number")
n=int(input())

if n%5==0 and n%7==0:
	print("divisible by both 5 and 7")
elif n%5==0 :
	print("divisible by only  5")
elif n%7==0:
	print("divisible by only 7")
else:
	print("not divisible by 5 and 7")

