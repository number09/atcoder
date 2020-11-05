li_s = list(input().split())
n = int(input())
li_t = []

for _ in range(n):
    li_t.append(input())

answer = []

def match(s, t):
    if len(s) == len(t):
        for w_s, w_t in zip(s, t):
            if w_s == w_t or w_t == '*':
                pass
            else:
                return False
        else:
            return True
    else:
        return False


for s in li_s:
    if any(match(s, t) for t in li_t):
        answer.append('*' * len(s))
    else:
        answer.append(s)

print(' '.join(answer))
