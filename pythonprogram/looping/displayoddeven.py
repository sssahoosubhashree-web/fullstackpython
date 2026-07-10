print("enter a number")
n=int(input())
even=0
odd=0
while(n!=0):
	digit=n%10
	if(digit %2 ==0):
   		even+=1
	else:
		odd+=1
	n=n//10	
print("total no.of even digit=",even)
print("total no.of odd digit=",odd)