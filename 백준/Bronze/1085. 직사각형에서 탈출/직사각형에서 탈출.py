x,y,w,h=list(map(int, input().split()))
a1=w-x
a2=x
b1=h-y
b2=y
print(min(a1,b1,a2,b2))