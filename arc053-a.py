h, w = map(int, input().split())
answer = 0
if h >= 2:
    answer += (h - 1) * w
if w >= 2:
    answer += (w - 1) * h
print(answer)
