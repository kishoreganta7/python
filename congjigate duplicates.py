#remove conjigate duplicates

s=input()
s1=s[0]
for i in range(1,lens(s)):
    if s[i-1]!=s[i]:
        s1+=s[i]
print(s1)
