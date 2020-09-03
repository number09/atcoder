n = int(input())

li_s = list()
for _ in range(n):
    li_s.append(input())

li_rev_s = list()
for s in li_s:
    li_rev_s.append(s[::-1])
li_ans = list()

for r in sorted(li_rev_s):
    li_ans.append(r[::-1])

for a in li_ans:
    print(a)
