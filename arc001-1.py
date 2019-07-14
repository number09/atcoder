n = int(input())
c = input()

res = [c.count(str(w)) for w in range(1, 5)]
print(max(res), min(res))
