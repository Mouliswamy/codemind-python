n=int(input())
m=int(input())
def pr(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else :
        return True
b=n+m
a=b+1
while pr(a)==False:
    a=a+1
print(a-b)
