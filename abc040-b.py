n = int(input())

s_answer = set()

for x in range(1, 1001):
    for y in range(1, 1001):
        rect = x * y
        amari = n - rect
        if amari >= 0:
            s_answer.add(abs(x - y) + amari)

print(min(s_answer))
