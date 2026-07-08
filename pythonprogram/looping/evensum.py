i=1
es=0
os=0
while(i<=10):
	if( i>5):
	  if(i%2==0):
		   es=es+i
	  else:
		   os=os+i
	i+=1
print("evensum=",es)
print("oddsum=",os)
