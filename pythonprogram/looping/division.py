print("enter two numbers")
n1=int(input())
n2=int(input())
d=0
while(n1>=n2):
	n1=n1-n2
	d=d+1
print("division=",d)
print("reminder=",n1)
