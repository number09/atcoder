s = input()
a, b, c, d = map(int, input().split())

li_ans = list()

for idx, w in enumerate(s):
    if idx in [a, b, c, d]:
        li_ans.append('"')
    li_ans.append(w)
if len(s) in [a, b, c, d]:
    li_ans.append('"')

print("".join(li_ans))
