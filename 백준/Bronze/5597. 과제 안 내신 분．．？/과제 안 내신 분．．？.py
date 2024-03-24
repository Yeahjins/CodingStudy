list_all=[]
for i in range(1,31):
    list_all.append(i)

list_B=[]
for i in range(28):
    N=int(input())
    if N in list_all:
        list_all.remove(N)
list_all.sort()
for i in range(2):
    print(list_all[i], end=' ')