N=int(input())
x_lst=[]
y_lst=[]
for i in range(N):
    x,y=map(int, input().split())
    x_lst.append(x)
    y_lst.append(y)
a=max(x_lst)-min(x_lst)
b=max(y_lst)-min(y_lst)
print(a*b)