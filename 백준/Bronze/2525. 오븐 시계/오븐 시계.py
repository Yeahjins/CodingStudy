a,b=map(int,input().split())
c=int(input())
c_h=c//60
c_m=c%60

a=a+c_h
b=b+c_m
if b>=60:
    a=a+1
    b=b-60
if a>=24:
    a=a-24

print(a,b)