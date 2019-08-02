replist = [
    ('O', '0'),
    ('D', '0'),
    ('I', '1'),
    ('Z', '2'),
    ('S', '5'),
    ('B', '8'),
           ]

s = input()

for r in replist:
    s = s.replace(r[0], r[1])
print(s)