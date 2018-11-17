n = int(input())
w = [1, 2, 4, 8]
result = list()

for i in sorted(w, reverse=True):
    if n // i > 0:
        result.append(i * (n // i))
    n = n % i
print(len(result))
for r in result:
    print(r)
