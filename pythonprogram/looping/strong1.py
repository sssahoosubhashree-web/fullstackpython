print("enter a number")
n=int(input())
temp=n
s=0
while (n!=0):
	d=temp%10
	m=1
	for i in range (1,d+1):
		m=m*i
	s=s+m
	n=n//10
if (temp==s):
	print ("Strong number =", s)
else:
	print ("Not a strong Number")
