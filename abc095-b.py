int_n, int_x = map(int, input().split())

int_m_ar = []
for m in range(int_n):
    int_m_ar.append(int(input()))

int_m_ar.sort()

count = 0
zan = int_x
for m in int_m_ar:
    count += 1
    zan -= m

for m in int_m_ar:
    count = count + int(zan / m)
    zan = zan - (m * int(zan / m))

print(count)

