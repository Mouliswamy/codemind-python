n=int(input())
m=int(input())
f=0
s=0
for i in range(1,n):
    if n%i==0:
        f=f+i
for j in range(1,m):
    if m%j==0:
        s=s+j
if f==m and s==n:
    print ('Amicable')
else:
    print('Not Amicable')