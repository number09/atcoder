l, x = map(int, input().split())

w = x % (l * 2)

print(w if w <= l else l - (w - l))