A=[]
for i in range(9):
    row=list(map(int, input().split()))
    A.append(row)

max=0
row=0
col=0
for i in range(9):
    for j in range(9):
        if A[i][j] >= max:
            max=A[i][j]
            row=i+1
            col=j+1
print(max)
print(row, col)