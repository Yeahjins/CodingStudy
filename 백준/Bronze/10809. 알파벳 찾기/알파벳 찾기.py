S=list(input())
mydict={}
for char in 'abcdefghijklmnopqrstuvwxyz':
    mydict[char] = -1

for i in range(len(S)):
    if S[i] in mydict.keys():
        if mydict[S[i]]==-1:
             mydict.update({S[i]:i})

values_list=list(mydict.values())
print(*values_list)