word=list(map(str,input().upper()))
word_dict=dict.fromkeys(word,0)
for i in range(len(word)):
    if word[i] in word_dict:
        word_dict[word[i]]+=1
max_key = [k for k,v in word_dict.items() if max(word_dict.values()) == v]
if len(max_key) != 1:
    print('?')
else:
    print(*max_key)