li_a = []

for i in range(5):
    li_a.append(max(int(input()), 40))

print(sum(li_a) // 5)
