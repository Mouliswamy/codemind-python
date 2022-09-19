n=int(input())
t=n
tem=n
i=0
s=0
a=len(str(n))
while tem!=0:
    r=tem%10
    tem=tem//10
    f=r**a
    a-=1
    s+=f
print(s==t)