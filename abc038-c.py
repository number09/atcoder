n = int(input())
li_a = list(map(int, input().split()))

result = 0
counter = 0
save_value = -1
# check index
for s in range(0, n):
    if save_value >= li_a[s]:
        result += sum(range(counter + 1))
        counter = 1
        save_value = li_a[s]
    else:
        counter += 1
        save_value = li_a[s]
else:
    result += sum(range(counter + 1)) if counter != -1 else 0

print(result)

