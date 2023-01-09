def sum_(x):
    s=0
    for i in range (1,x):
        if x%i==0:
            s=s+i
    return s
n= int(input())
m=int(input())
if sum_(n)==m or sum_(m)==n:
    print("Amicable")
else :
    print("Not Amicable")
        