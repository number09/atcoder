s = input()
answer = 0
li_s = list(s.split("+"))

for w in li_s:
    if len(w) == 1:
        if w == "0":
            pass
        else:
            answer += 1
    else:
        if "0" in w:
            pass
        else:
            answer += 1
print(answer)
