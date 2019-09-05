li_s = input().split()

li_ans = list()

for w in li_s:
    if w == "Left":
        li_ans.append("<")
    elif w == "Right":
        li_ans.append(">")
    else:
        li_ans.append("A")
print(" ".join(li_ans))
