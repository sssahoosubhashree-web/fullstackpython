print("enter three number")
n1=int(input())
n2=int(input())
n3=int(input())
if n1>=n2:
	if n1>=n3:
		print(n1,"first number is bigger")
	else:
		print(n3,"third number is bigger")
else:
	if n2>=n3:
		print(n2,"first number is bigger")
	else:
		print(n3,"third number is bigger")
