s = input()
k = int(input())

w = k % len(s)

for _ in range(w):
    s = s[1:] + s[0]
print(s)

