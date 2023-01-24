def pr(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
def prepr(n):
    a=n
    while pr(a)==False:
        a=a-1
    return a
def afpr(n):
    a=n
    while pr(a)==False:
        a=a+1
    return a
def nepr(n):
    a=prepr(n)
    b=afpr(n)
    if n-a<=b-n:
        print(n-a)
    else:
        print(b-n)
a=int(input())
nepr(a)
