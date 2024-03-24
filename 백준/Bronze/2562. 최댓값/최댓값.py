list=[]
for i in range(9):
    N=int(input())
    list.append(N)

n=0 
a=0
for j in range(0,len(list)):
    if list[j] > a:
        a=list[j]
        n=j+1
print(a)
print(n)