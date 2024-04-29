N = int(input())
M = list(map(int, input().split()))
result = 0

for N in M:
    cnt = 0
    if N > 1:
        for i in range(2, N):
            if N % i == 0:
                cnt += 1
        
        if cnt == 0:
            result += 1
    
print(result)