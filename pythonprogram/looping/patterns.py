1   2  3  4

print("1 2  3 4 ")


1 2 3 4 5

print("1 2  3 4 5")


1 2 3 4

j=1
while j<=4:
	print(j,end="\t")
	j=j+1


1 2 3 4 5

j=1
while j<=5:
	print(j,end="\t")
	j=j+1

1 2 3 4
c=4
j=1
while j<=c:
	print(j,end="\t")
	j=j+1

print("enter a range ")
c=int(input())
j=1
while j<=c:
	print(j,end="\t")
	j=j+1


1 2 3 4
for j in range(1,5,1):
	print(j,end="\t")


/*
in c ,c++,java

int j;
for(j=1;j<5;j++)
{
	//System.out.print(j+"\t");
	printf("%d\t",j);
	//cout<<j<<"\t";
}



for j in range(1,5,1):
	print("hi",end="\t")

o/p:
hi hi hi hi


for j in range(1,5,1):
	print(1,end="\t")

o/p:
1 1 1 1 

for j in range(1,5,1):
	print(j,end="\t")

o/p:
1 2 3 4
for j in range(4,0,-1):
	print(j,end="\t")
o/p:
4 3 2 1






1 2 3 4
1 2 3 4
1 2 3 4

for i in range(1,4,1):
	for j in range(1,5,1):
		print(j,end="\t")
	print()

* * * *
* * * *
* * * *

for i in range(1,4,1):
	for j in range(1,5,1):
		print("*",end="\t")
	print()


1 1 1 1
2 2 2 2
3 3 3 3
for i in range(1,4,1):
	for j in range(1,5,1):
		print(i,end="\t")
	print()


4 3 2 1
4 3 2 1
4 3 2 1

for i in range(1,4,1):
	for j in range(4,0,-1):
		print(j,end="\t")
	print()

3 3 3 3 
2 2 2 2
1 1 1 1

for i in range(3,0,-1):
	for j in range(4,0,-1):
		print(i,end="\t")
	print()





rule:
big row print first
second big row print first big row change 
third where 
first row print i value need  

i value may be 1    1,5,1
i value may be 4    4,0,-1


1
1 2
1 2 3
1 2 3 4
for i in range(1,5,1):
	for j in range(1,i+1,1):
		print(j,end="\t")
	print()

 1 2 3 4
 1 2 3
 1 2
 1

for i in range(4,0,-1):
	for j in range(1,i+1,1):
		print(j,end="\t")
	print()

4 3 2 1
4 3 2
4 3
4
for i in range(1,5,1):
	for j in range(4,i-1,-1):
		print(j,end="\t")
	print()

4
4 3
4 3 2
4 3 2 1

for i in range(4,0,-1):
	for j in range(4,i-1,-1):
		print(j,end="\t")
	print()

1
2 1
3 2 1
4 3 2 1

for i in range(1,5,1):
	for j in range(i,0,-1):
		print(j,end="\t")
	print()

4 3 2 1
3 2 1
2 1
1

for i in range(4,0,-1):
	for j in range(i,0,-1):
		print(j,end="\t")
	print()


4
3 4
2 3 4
1 2 3 4
for i in range(4,0,-1):
	for j in range(i,5,1):
		print(j,end="\t")
	print()


1 2 3 4
2 3 4
3 4
4
for i in range(1,5,1):
	for j in range(i,5,1):
		print(j,end="\t")
	print()