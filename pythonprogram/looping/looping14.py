i=1
es=0
os=0
while(i<=10):
	if( i>5 and i%2==0):
		es=es+i
	if(i>5 and i%2!=0):
		os=os+i
	i+=1
print("evensum=",es)
print("oddsum=",os)
