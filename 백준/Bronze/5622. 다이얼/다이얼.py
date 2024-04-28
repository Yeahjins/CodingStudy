phone=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
num=list(input())
sum=0
for i in range(len(num)):
    for j in range(len(phone)):
        if num[i] in phone[j]:
            sum=sum+(j+3)
print(sum)