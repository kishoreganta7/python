#write a python program  to print a numbers which are not divisible ny 6 ,7and 8in given range

for i in range(1,100,1):
    if i%2!=0 and i%6!=0 and i%7!=0 and i%8!=0:
        
        print(i)
