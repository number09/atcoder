n = int(input())
set_a = set()
for i in range(n):
    set_a.add(int(input()))

print(sorted(list(set_a), reverse=True)[1])
