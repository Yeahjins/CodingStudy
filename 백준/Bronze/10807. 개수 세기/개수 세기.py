N=int(input())
number = list(map(int, input().split()))
v=int(input())
cnt=0
i=0
for i in range(N):
    if number[i] == v:
        cnt += 1
print(cnt)