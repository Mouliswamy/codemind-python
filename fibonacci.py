n=int(input())
a=0
b=1
s=a+b
print(a,b,s,end=' ')
for i in range(n-3):
    a=b
    b=s
    s=a+b
    print(s,end=' ')