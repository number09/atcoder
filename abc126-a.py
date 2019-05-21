n, k = map(int, input().split())
s = input()

w = s[k - 1].lower()

print("".join([s[:k - 1], w, s[k:]]))
