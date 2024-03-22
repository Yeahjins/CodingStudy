T=int(input())
cnt=0
while cnt<T:
    A,B=map(int, input().split())
    sum=A+B
    print('Case #{0}: {1}'.format(cnt+1,sum))
    cnt+=1