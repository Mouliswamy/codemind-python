n=int(input())
l=list(map(int,input().split()))
a=0
m=sum(l)//n
for i in l:
    if i>=m:
        a+=1
print(a)