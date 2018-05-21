str_s = input()
int_k = int(input())

pattern = set()

for f in range(len(str_s) + 1):
    for t in range(f + 1, len(str_s) + 1):
        pattern.add(str_s[f:t])

print(sorted(list(pattern))[int_k - 1])


