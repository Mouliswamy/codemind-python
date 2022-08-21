def divisor(n):
    k=n
    s=0
    while n>0:
        r=n%10
        if r==0:
            return False
        if k%r==0:
            s=s+1
        n=n//10
    if s==len(str(k)):
        return True
    else :
        return False
x=int(input())
y=int(input())
for i in range(x,y+1):
    if divisor(i)==True:
        print(i,end=' ')