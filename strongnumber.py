#write a python program given number strong number or not

def strong(n):
    x,sum=n,0
    while n>0:
        digit=n%10
        fact=1
        for i in range(1,digit+1):
            fact*=i
        sum+=fact
        n//=10
    if sum == x:
        return "strong number"
    else:
        return "not strong number"
n=int(input("enter a number:"))
print(strong(n))
