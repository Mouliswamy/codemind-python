def h(n):
    s=0
    while n>0:
        r=n%10
        s=s+r**2
        n=n//10
    return s
x= int(input())
ha=1
while x>9:
    x=h(x)
if x==ha:
    print(True)
else:
    print(False)