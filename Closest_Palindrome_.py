def pali(n):
    s=0
    k=n
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    if k==s:
        return True
    else:
        return False
def prepali(n):
    while pali(n)!=True:
        n=n-1
    return(n)
def nextpali(n):
    while pali(n)!=True:
        n=n+1
    return(n)
x=int(input())
p=prepali(x)
q=nextpali(x)
if pali(x)==True:
    print(prepali(x-1),nextpali(x+1))
elif x-p<q-x:
    print(p)
elif x-p>q-x:
    print(q)
elif x-p==q-x:
    print(p,q)