h, w = map(int, input().split())
li_s = []

for i in range(h):
    li_s.append(input())

answer = 0
for w_h in range(0, h):
    for w_w in range(0, w):
        if li_s[w_h][w_w] == '.':
            if w_w != w - 1:
                if li_s[w_h][w_w + 1] == '.':
                    answer += 1
            if w_h != h - 1:
                if li_s[w_h + 1][w_w] == '.':
                    answer += 1
print(answer)