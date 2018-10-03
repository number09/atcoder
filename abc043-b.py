s = input()

result = list()

for w in s:
    if w == "B":
        if len(result):
            result.pop()
    else:
        result.append(w)
print("".join(result))


