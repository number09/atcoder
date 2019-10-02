n = int(input())
li_a = list(map(int, input().split()))

li_wk = sorted([(idx, a) for idx, a in enumerate(li_a)], key=lambda x:x[1])

print(" ".join(str(w[0] + 1) for w in li_wk))
