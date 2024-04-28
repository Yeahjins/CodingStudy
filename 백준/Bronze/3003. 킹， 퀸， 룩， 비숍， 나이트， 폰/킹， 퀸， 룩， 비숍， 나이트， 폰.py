c=list(map(int,input().split()))
ori=[1,1,2,2,2,8]
a=0
sub=[]
for i in range(6):
    a=ori[i]-c[i]
    sub.append(a)
print(*sub)