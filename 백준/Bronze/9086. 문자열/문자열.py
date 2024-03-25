T=int(input())
word_list=[]
for i in range(T):
    word=input()
    word_list.append(word)

for j in range(len(word_list)):
    if len(word_list[j])==1:
        print(word_list[j]*2)
    else:
        print(word_list[j][0]+word_list[j][-1])