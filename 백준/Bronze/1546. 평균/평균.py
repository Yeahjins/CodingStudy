N=int(input())
score=list(map(int, input().split()))
score.sort()
sum=0
for i in range(N):
    score[i]=score[i]/score[N-1]*100
    sum=sum+score[i]
print(sum/N)