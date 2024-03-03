#write python program using functions in range


def primenumber(n,m):
    for i in range(n,m+1):
        c=0
        for j in range(1,i+1):
            if i%j==0:
                c+=1
        if c==2:
            
            print(i)
n,m=int(input("enter first number in range:")),int(input(" enter last number in range:"))
primenumber(n,m)
    

