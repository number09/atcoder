li_a = []
li_b = []

for i in range(4):
    li_a.append(int(input()))

for i in range(2):
    li_b.append(int(input()))

print(
    sum(list(sorted(li_a, reverse=True))[:3]) +
    list(sorted(li_b, reverse=True))[0]
)
