a,b,c=list(map(int, input().split()))
lst=[]
lst.extend([a,b,c])

if (sum(lst)-max(lst)) <= max(lst):
    print(2*(sum(lst)-max(lst))-1)
else:
    print(sum(lst))