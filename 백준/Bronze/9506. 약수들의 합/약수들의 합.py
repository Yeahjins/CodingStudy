while True:
    lst=[]
    sum=0
    N=int(input())
    if N==-1:
        break
    else:
        for i in range(1,N):
            if int(N)%i==0:
                lst.append(i)
                sum=sum+i
        if N==sum:
            print(N,'= ', end='')
            print(*lst,sep=' + ')
        else:
            print(N, 'is NOT perfect.')