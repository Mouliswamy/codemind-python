x,y=map(int,input().split())
i=0
while i<=y:
    i=i+1
    if (x*i)%y==0:
        print(x*i)
        break
