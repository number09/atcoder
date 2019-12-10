s = input()
count = 0
for x, y in zip(s, s[::-1]):
    if x != y:
        count += 1
print(count // 2)
