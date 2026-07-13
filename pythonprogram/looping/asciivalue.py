print("enter a character")
ch=input()
if len(ch)!=1:
	print("single chracter allowed")
	sys.exit()
print(ch)
print(ord(ch))