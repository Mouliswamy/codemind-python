x=int(input())
i=0
while i<=x:
    i=i+1
    if i*i==x:
        print(True)
        break
else:
    print(False)