n, p = map(int, input().split())

li_a = list(map(int, input().split()))
counter = 0
for a in li_a:
    if p >= a:
        p -= a
        counter += 1
    else:
        break
print(counter)