a, b, c = map(int, input().split())

d = {a: 'A', b: 'B', c: 'C'}

print(d.get(sorted([a, b, c])[1]))
