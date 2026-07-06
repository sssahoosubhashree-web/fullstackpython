print("enter a number")
l=float(input())
print("enter second number")
b=float(input())
print("enter your choice 1,rectangle")
print(" enter your choice2,sqaure")
print(" enter your choice3,circle area")
print(" enter your choice 4,invalid")
ch =int(input())
if ch==1:
	print("rectangle=",l*b)
elif ch==2:
	print("square",l*l)
elif ch==3:
	print("enter  a radius")
	r=float(input())
	print("circle area",3.14*r*r)
else:
   print("invalid choice")