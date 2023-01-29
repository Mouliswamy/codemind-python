n=int(input())
l=list(map(int,input().split()))
o=0 
e=0
for i in l :
    if i%2==0:
        e+=i
    else:
        o+=i
print(abs(e-o))