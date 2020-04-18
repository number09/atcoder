import math


k = int(input())
answer = 0
for w_a in range(1, k + 1):
    for w_b in range(1, k + 1):
        w = math.gcd(w_a, w_b)
        for w_c in range(1, k + 1):
            answer += math.gcd(w, w_c)

print(answer)
