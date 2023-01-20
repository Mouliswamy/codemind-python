def rev(n):
    s=0
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    return s
def sq(n):
    a=n*n
    return(a)
a=int(input())
b=rev(a)
c=sq(a)
d=sq(b)
if c==rev(d):
    print(True)
else:
    print(False)