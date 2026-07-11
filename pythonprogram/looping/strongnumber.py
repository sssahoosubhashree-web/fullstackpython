print("enter a number")
n=int(input())
temp=n
s=0
while temp>0:
	r=temp%10
	f=1
	while r>0:
		f=f*r
		r=r-1
	s=s+f
	temp=temp//10
if s==n:
	print("strong number")
else:
	print("not strong number ")