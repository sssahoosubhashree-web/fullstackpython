print("Enter any number")
n=int(input())
even=0
odd=0
while (n!=0):
	d=n%10
	if (d%2==0):
		even = even+d
	else:
		odd = odd+d 
	n=n//10
sum=even+odd
print("Sum of even,odd digits are =", even,"+",odd)
print ("Total sum of all digits are =", sum)
