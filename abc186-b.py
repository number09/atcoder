h, w = map(int, input().split())

goukei = 0
mini = 100
for w_h in range(h):
    li_w = list(map(int, input().split()))
    mini = min(min(li_w), mini)
    goukei += sum(li_w)
print(goukei - (mini * h * w))
