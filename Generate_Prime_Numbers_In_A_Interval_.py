def pr(n):
    for i in range(2,n):
        if n%i==0:
            return False
    else :
        return True
m=int(input())
n=int(input())
l=[]
for i in range(m,n+1):
    if pr(i)==True:
        if i==1:
            pass
        else:
            l.append(i)
for i in l:
    print(i)
