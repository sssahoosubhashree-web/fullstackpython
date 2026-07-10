print("enter  any 3 digit number")
n=int(input())
d=n
s=0
while(d!=0):
  digit=d%10
  s=s+digit**3
  d=d//10
print("sum=",s)
if(s==n):
	print("Armstrong number")
else:
	print("not armstrong number")