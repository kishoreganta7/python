#write python program to print given number is prime or not

n=int(input("enter a number:"))
count=0
for i in range(1,n):
    if (n%i==0):
        count+=1
if count>=2:
    print(" it is not prime")
else:
    print("it is a prime")




        
    
