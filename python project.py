#cack question 


cakeangle=eval(input("enter the angle of the cake: "))
N=eval(input("enter N: "))
if(cakeangle%N==0)
    print("yes the cake will cut in equal pieces of size %d"%N)
else:
    print ("NO the cake will not cut in equal pieces of size %d %N")
if(N>cakeangle): #only when N is greater tha cake angle cake can't be cut into pieces
    print("NO the cake will not cut in any pieces of size %d"%N)
else:
    print("yes the cake will cut in any piece of size %d"%N)
n=1 # start subratcrting the cake 
for i in range(N)
    cakeangle-=N
    n+=1
    if(cakeangle<0):
        print("no the cake will cut into %d pieces such that no two of them are equal"%N) 
        break
else:
        print("yes te cake will cut into %d pieces such that no two of them are equal%N")      
            