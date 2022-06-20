height=int(input("height :"))
for i in range (1,height+1):
    for j in range(height -i,0,-1):
        print(" ",end="")
    for o in range(i):
        print("#",end="")
    print('  ',end="")
    for o in range(i):
        print("#",end="")
    print('')