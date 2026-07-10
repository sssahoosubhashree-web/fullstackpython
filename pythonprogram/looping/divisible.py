print("enter a number")
num=int(input())
i=1
print("Divisors are :")
while(i<=num//2):
	if num%i==0:
		print(i)
	i=i+1
