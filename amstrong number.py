#write python to print amstrong number 

n=int(input("entetr a number:"))
temp=n
rev=0
while n>0:
    digit=n%10
    rev=rev+digit**3
    n//=10
if rev == temp:
    print("amstrong")
else:
    print("not amstrong")
