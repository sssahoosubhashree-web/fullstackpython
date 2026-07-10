print("enter a number")
n=int(input())
d=n
rev=0
while(n!=0):
	digit=n%10
	rev=rev*10+digit
	n=n//10
if(d==rev):
   print("palindrome")
else:
   print("not palindrome")