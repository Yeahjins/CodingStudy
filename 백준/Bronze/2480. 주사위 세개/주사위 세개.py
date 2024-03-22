a,b,c=map(int,input().split())
li=[]
li.extend([a,b,c])
li.sort()
same=0
cnt=0
for i in range(0,3):
    for j in range(i+1,3):
        if li[i] == li[j]:
            same=li[j]
            cnt+=1
    
if cnt==0:
    print(li[2]*100)
elif cnt==1:
    print(1000+same*100)
elif cnt==3:
    print(10000+same*1000)