list_A = []
for i in range(10):
    A=int(input())
    B=A%42
    if B not in list_A:
        list_A.append(B)
print(len(list_A))