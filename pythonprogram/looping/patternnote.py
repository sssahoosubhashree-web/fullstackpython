A   B C D

for j in range(65,69,1):
	print(chr(j),end="\t")


D C B A

for j in range(68,64,-1):
	print(chr(j),end="\t")


A   B C D
A   B C D
A   B C D
for i in range(1,4,1):
	for j in range(65,69,1):
		print(chr(j),end="\t")
	print()


A   B C D
A   B C D
A   B C D
for i in range(65,68,1):
	for j in range(65,69,1):
		print(chr(j),end="\t")
	print()


A A A A
B B B B 
C C C C

for i in range(65,68,1):
	for j in range(65,69,1):
		print(chr(i),end="\t")
	print()

C C C C
B B B B
A A A A
for i in range(67,64,-1):
	for j in range(65,69,1):
		print(chr(i),end="\t")
	print()

A
A B
A B C
A B C D




for i in range(65,69,1):
	for j in range(65,i+1,1):
		print(chr(j),end="\t")
	print()


A B C D
A B C
A B
A

for i in range(68,64,-1):
	for j in range(65,i+1,1):
		print(chr(j),end="\t")
	print()

D C B A
D C B
D C
D

for i in range(65,69,1):
	for j in range(68,i-1;-1):
		print(chr(j),end="\t")
	print()


D
D C
D C B
D C B A
for i in range(68,64,-1):
	for j in range(68,i-1;-1):
		print(chr(j),end="\t")
	print()



A
B A
C B A
D C B A


for i in range(65,69,1):
	for j in range(i,64,-1):
		print(chr(j),end="\t")
	print()

D C B A
C B A
B A
A

for i in range(68,64,-1):
	for j in range(i,64,-1):
		print(chr(j),end="\t")
	print()

D
C D
B C D
A B C D

for i in range(68,64,-1):
	for j in range(i,69,1):
		print(chr(j),end="\t")
	print()
A B C D
B C D
C D
D

for i in range(65,69,1):
	for j in range(i,69,1):
		print(chr(j),end="\t")
	print()

Left space
-------------

1
12
123
1234
1234
123
12 
1
for i in range(1,5,1):
	for j in range(1,i+1,1):
		print(j,end="")
	print()
for i in range(4,0,-1):
	for j in range(1,i+1,1):
		print(j,end="")
	print()


1
21
321
4321
321
21
1
for i in range(1,5,1):
	for j in range(i,0,-1):
		print(j,end="")
	print()
for i in range(3,0,-1):
	for j in range(i,0,-1):
		print(j,end="")
	print()

   1
  12
 123
1234

for i in range(1,5,1):
	for j in range(4-i,0,-1):
		print(end=" ")
	for j in range(1,i+1,1):
		print(j,end="")
	print()



   1
  12
 123
1234

for i in range(1,5,1):
	for j in range(1,5-i,1):
		print(end=" ")
	for j in range(1,i+1,1):
		print(j,end="")
	print()

1234
 123
  12
   1

for i in range(4,0,-1):
	for j in range(4-i,0,-1):
		print(end=" ")
	for j in range(1,i+1,1):
		print(j,end="")
	print()



   11
  1221
 123321
12344321

for i in range(1,5,1):
	for j in range(4-i,0,-1):
		print(end=" ")
	for j in range(1,i+1,1):
		print(j,end="")
	for j in range(i,0,-1):
		print(j,end="")
	print()

   1
  121
 12321
1234321

for i in range(1,5,1):
	for j in range(4-i,0,-1):
		print(end=" ")
	for j in range(1,i+1,1):
		print(j,end="")
	for j in range(i-1,0,-1):
		print(j,end="")
	print()


   1
  121
 12321
1234321
1234321
 12321
  121
   1

for i in range(1,5,1):
	for j in range(4-i,0,-1):
		print(end=" ")
	for j in range(1,i+1,1):
		print(j,end="")
	for j in range(i-1,0,-1):
		print(j,end="")
	print()
for i in range(4,0,-1):
	for j in range(4-i,0,-1):
		print(end=" ")
	for j in range(1,i+1,1):
		print(j,end="")
	for j in range(i-1,0,-1):
		print(j,end="")
	print()



   1
  121
 12321
1234321
1234321
 12321
  121
   1

r=4
for i in range(1,r+1,1):
	for j in range(r-i,0,-1):
		print(end=" ")
	for j in range(1,i+1,1):
		print(j,end="")
	for j in range(i-1,0,-1):
		print(j,end="")
	print()
for i in range(r,0,-1):
	for j in range(r-i,0,-1):
		print(end=" ")
	for j in range(1,i+1,1):
		print(j,end="")
	for j in range(i-1,0,-1):
		print(j,end="")
	print()



   1
  121
 12321
1234321
 12321
  121
   1

r=4
for i in range(1,r+1,1):
	for j in range(r-i,0,-1):
		print(end=" ")
	for j in range(1,i+1,1):
		print(j,end="")
	for j in range(i-1,0,-1):
		print(j,end="")
	print()
for i in range(r-1,0,-1):
	for j in range(r-i,0,-1):
		print(end=" ")
	for j in range(1,i+1,1):
		print(j,end="")
	for j in range(i-1,0,-1):
		print(j,end="")
	print()


 middle space
 ------------------
12344321
123  321
12    21
1      1

sp=0
for i in range(4,0,-1):
	for j in range(1,i+1,1):
		print(j,end="")
	for j in range(0,sp,1):
		print(end=" ")
	for j in range(i,0,-1):
		print(j,end="")
	sp=sp+2
	print()

12344321
123  321
12    21
1      1
1      1
12    21
123  321
12344321
for i in range(4,0,-1):
	for j in range(1,i+1,1):
		print(j,end="")
	for j in range(0,sp,1):
		print(end=" ")
	for j in range(i,0,-1):
		print(j,end="")
	sp=sp+2
	print()
sp=sp-2
for i in range(1,5,1):
	for j in range(1,i+1,1):
		print(j,end="")
	for j in range(0,sp,1):
		print(end=" ")
	for j in range(i,0,-1):
		print(j,end="")
	sp=sp-2
	print()





1
00
111
0000

for i in range(1,5,1):
	for j in range(1,i+1,1):
		print(i%2,end="")
	print()


0
11
000
1111


for i in range(1,5,1):
	for j in range(1,i+1,1):
		print((i+1)%2,end="")
	print()

1
1 0
1 0 1
1 0 1 0

for i in range(1,5,1):
	for j in range(1,i+1,1):
		print(j%2,end="")
	print()

0
0 1
0 1 0
0 1 0 1

for i in range(1,5,1):
	for j in range(1,i+1,1):
		print((j+1)%2,end="")
	print()


0
1 0
0 1 0
1 0 1 0

for i in range(1,5,1):
	for j in range(1,i+1,1):
		print((i+j)%2,end="")
	print()
1
0 1
1 0 1
0 1 0 1

for i in range(1,5,1):
	for j in range(1,i+1,1):
		print((i+j+1)%2,end="")
	print()



1
00
111
0000

for i in range(1,5,1):
	for j in range(1,i+1,1):
		if i%2==0:
			print("0",end="")
		else:
			print("1",end="")
	print()

@
##
@@@
####

for i in range(1,5,1):
	for j in range(1,i+1,1):
		if i%2==0:
			print("#",end="")
		else:
			print("@",end="")
	print()

1
2 3
4 5 6
7 8 9 10

c=0
for i in range(1,5,1):
	for j in range(1,i+1,1):
		c=c+1
		print(c,end="\t")
	print()

A
B C
D E F
G H I J

c=64
for i in range(1,5,1):
	for j in range(1,i+1,1):
		c=c+1
		print(chr(c),end="\t")
	print()


ABCDDCBA
ABCCBA
ABBA
AA


ABCD
 ABC
  AB
   A

 g
 g o
 g o p
 g o p a
 g o p a l

s="gopal"
for i in range(0,len(s),1):
	for j in range(0,i+1,1):
		print(s[j],end=" ")
	print()