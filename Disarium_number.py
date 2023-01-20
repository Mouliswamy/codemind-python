n=int(input())
b=n
s=0
a=len(str(n))
while b>0:
    r=b%10
    d=r**a
    a=a-1
    s=s+d
    b=b//10
print(s==n)
    
    