s = input()

li_out = list()

for w in s:
    if w == "O":
        li_out.append("A")
    elif w == "A":
        li_out.append("O")
    else:
        li_out.append(w)
print("".join(li_out))

