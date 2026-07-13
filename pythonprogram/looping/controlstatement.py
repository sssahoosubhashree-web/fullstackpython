contole statement
__________________
sequentional 
____________________
print("A")
print("B")
print("C")


o/p:
A
B
C

above program this style   (simple interset,add,mark program)

condtional
______________
if 
if else
elif
match case

looping
___________
while
for in

jumping
_________
break
continue


if condtion:
	.....
	......
	.......
or

if(condtion):
	.....
	......
	.......


a=5
if a>4:
	a=10
print(a)


o/p:
10


a=5
if a<4:
	a=10
print(a)

o/p:
5


if True:
	print("A")
print("B")

o/p:
A
B

if False:
	print("A")
print("B")

o/p:
B



if 5:
	print("A")
print("B")

o/p:
A
B

if 0:
	print("A")
print("B")

o/p:
B






if "hi":
	print("A")
print("B")

o/p:
A
B

if "":
	print("A")
print("B")

o/p:
B



#wap take a number from keyboard check no is +ve
print("enter a number ")
no=int(input())
if no>0:
	print("+ve")

o/p:
enter a number
5
+ve
o/p:
enter a number
-2


#wap take a number from keyboard check no is -ve
print("enter a number ")
no=int(input())
if no<0:
	print("-ve")

#wap take a number from keyboard check no is zero
print("enter a number ")
no=int(input())
if no==0:
	print("zero")


#wap take a number from keyboard check no is nonzero
print("enter a number ")
no=int(input())
if no!=0:
	print("zero")


#wap take a number from keyboard check no is even no
print("enter a number ")
no=int(input())
if no%2==0:
	print("even no")

#wap take a number from keyboard check no is odd no
print("enter a number ")
no=int(input())
if no%2!=0:
	print("odd no")

#wap take emp sal from keyboard if sal>=5000  da=30% hra=20% then display basic sal da hra and total sala

print("enter a basic ")
sal=float(input())
da,hra=0,0
if sal>=5000:
	da=sal*0.3
	hra=sal*0.2
total=sal+da+hra
print("basic sal=",sal)
print("da=",da)
print("hra=",hra)
print("total sal=",total)


multiple if
______________
program contain more than if every if condtion must be checking

if True:
	print("A")
if False:
	print("B")
if True:
	print("C")

o/p:
AC


#wap take a no from keyboard check no is +ve -ve and zero
print("enter a number ")
no=int(input())
if no>0:
	print("+ve")
if no<0:
	print("-ve")
if no==0:
	print("zero")


#wap take two no from keyborad check both no same 1st>2nd  2nd>1st

print("enter a number ")
no1=int(input())
print("enter another number ")
no2=int(input())
if no1==no2:
	print("same")
if no1>no2:
	print("1st>2nd")
if no1<no2:
	print("2nd>1st")


#wap take a nagtive number convert to +ve 
print("enter a number ")
no=int(input())
if no<0:
	no=-no
print(no)


nested if
________________
if   c1:
	.....
	if  c2:
		......

	.....
###


if True:
	print("A")
	if True:
		print("B")
	print("C")
print("D")


o/p:
A
B
C
D

if False:
	print("A")
	if True:
		print("B")
	print("C")
print("D")


o/p:
D

if True:
	print("A")
	if False:
		print("B")
	print("C")
print("D")


o/p:
A
C
D

#wap take a no from keyboars check no is 2 digit number
print("enter a no ")
no=int(input())
if no>9:
	if no<100:
		print("two digit number")


#wap take a no from keyboars check no is 2 digit number
print("enter a no ")
no=int(input())
if no>9 and no<100:
	print("two digit number")


#wap take a no from keyboars check no is 2 digit number
print("enter a no ")
no=int(input())
if no<0:
	no=-no
if no>9 and no<100:
	print("two digit number")





#wap take a no from keyboars check no is 2 digit number
print("enter a no ")
no=int(input())
if no<0:
	no=-no
if 9<no<100:
	print("two digit number")


if else
__________
if  condtion:
	....if block....
else:
	....else block ....


if True:
	print("A")
else:
	print("B")
print("C")

o/p:
A
C

if False:
	print("A")
else:
	print("B")
print("C")

o/p:
B
c


a=5
if a>4:
	a=10
else:
	a=7
print(a)

o/p:
10


a=3
if a>4:
	a=10
else:
	a=7
print(a)

o/p:
7


#wap check no is +ve or -ve using if else

print("enter a number ")
no=int(input())
if no>=0:
	print("+ve")
else:
	print("-ve")

using if else
#wap check no is zero or non zero
#wap check no is even or odd 
#wap take emp sal from keyboard if sal>=5000 da=30% hra=20% id sal<5000
da=10% hra=15% then display basic sal da hra and total sal
#wap take a person age from keyboard check person eligbal voteing or not
#wap  take two no from keyboard check both nos are same or differnent