str_s = input()
int_k = int(input())

result = list()
for f in range(len(str_s)):
    pattern = set()
    for t in range(f + 1, f + 1 + int_k):
        pattern.add(str_s[f:t])
        result = sorted(set(result + list(pattern)))[:int_k]

print(result[-1])

