def pr(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else :
        return True
n=int(input())
a=1
for i in range(1,n+1):
    if n%i==0 and pr(i)==False:
        a=a+1
print(a)