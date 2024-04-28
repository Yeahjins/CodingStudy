N,M=input().split()
lst=[]

for i in range(1,int(N)+1):
    if int(N)%i==0:
        lst.append(i)

if len(lst) >= int(M):
    print(lst[int(M)-1])
else:
    print(0)