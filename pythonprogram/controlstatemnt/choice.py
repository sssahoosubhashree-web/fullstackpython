print("enter a number")
n1=int(input())
print("enter second number")
n2=int(input())
print("enter your choice 1,addition")
print(" enter your choice2,subtraction")
print(" enter your choice3,multiplication")
print(" enter your choice 4,division")
ch =int(input())
if ch==1:
	print("addition=",n1+n2)
elif ch==2:
	print("subtraction",n1-n2)
elif ch==3:
	print("multiplication",n1*n2)
else:
   print("invalid choice")