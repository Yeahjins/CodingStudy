T=int(input())
cnt=0
while cnt<T:
    A,B=map(int, input().split())
    C=A+B
    print('Case #{0}: {1} + {2} = {3}'.format(cnt+1,A,B,C))
    cnt+=1