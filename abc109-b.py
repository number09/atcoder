int_n = int(input())

li_words = list()
for i in range(int_n):
    li_words.append(input())

ends = "".join([e[-1] for e in li_words[:-1]])
starts = "".join([s[0] for s in li_words[1:]])

if starts == ends and len(set(li_words)) == int_n:
    print("Yes")
else:
    print("No")
