def pr(n):
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    else:
        return True
a=int(input())
mg=True
if pr(a)==True:
    while a>0:
        r=a%10
        if pr(r)==False:
            mg=False
            break
        a=a//10
    else:
        mg=True
    if mg==True :
        print('Mega Prime')
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")