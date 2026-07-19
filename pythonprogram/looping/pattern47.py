for i in range(4,0,-1):
    for j in range(i):
        print(chr(65+j),end="")
    for j in range(i-1,-1,-1):
        print(chr(65+j),end="")
    print()