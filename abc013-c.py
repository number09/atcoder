n, h = map(int, input().split())

a, b, c, d, e = map(int, input().split())


answer = n * a

for count_a in range(n + 1):
    for count_c in range(n + 1):
        if count_a * b + count_c * d + h - (n - count_a - count_c) * e >= 1:
            if count_a * a + count_c * c < answer:
                answer = count_a * a + count_c * c
            break

print(answer)
