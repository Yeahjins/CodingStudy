H,M=map(int, input().split())
if (M>=45):
    print(H, M-45)
elif (M<45) & (H!=0):
    m = 60-(45-M)
    print(H-1,m)
elif (M<45) & (H==0):
    m = 60-(45-M)
    print(23, m)