n=int(input())
if n<0:
    n=-n
    m=1
else:
    n=n
    m=0
s=0
while n>0:
    r=n%10
    s=s*10+r
    n=n//10
if m==1:
    print(-1*s)
else :
    print(s)