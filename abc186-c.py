n = int(input())

w_set = set()
for i in range(1, n + 1):
    if '7' in str(i):
        w_set.add(i)
    elif '7' in oct(i):
        w_set.add(i)
print(n - len(w_set))
