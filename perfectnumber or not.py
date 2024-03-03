#write program to given number is perfect or not


n=int(input("enter a number:"))
sum=0
for i in  range(1,n):
    if (n%i==0):
        sum+=i
if sum==n:
    print("it is a pefect number")
else:
    print("not perfect")
