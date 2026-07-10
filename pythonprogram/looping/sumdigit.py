print ("Enter any number")
n=int(input())
s=0
while(n!=0):
	d=n%10
	s=s+d
	n=n//10
print ("Sum of all digits of a number=",s)
