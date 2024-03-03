x=int(input("no of friends:"))
y=int(input("no of pieces:"))
a=x*y
h=a%4
if h==0:
    print(a//4)
else:
    print((a//4)+1)
    

