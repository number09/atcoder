s = input()
k = int(input())

pattern = set()

for i in range(len(s) - k + 1):
    pattern.add(s[0 + i:k + i])

print(len(pattern))
