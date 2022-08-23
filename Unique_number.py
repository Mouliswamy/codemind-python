n=int(input())
tem=n
t=n
f=0
while tem>0:
    r=tem%10
    t=n
    c=0
    while t!=0:
        rem=t%10
        if rem==r:
            c=c+1
        if c>1:
            f=1
            break
        t=t//10
    tem=tem//10
if f==0:
    print('Unique Number')
else:
    print('Not Unique Number')
