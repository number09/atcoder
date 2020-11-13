n = int(input())
li_a = list(map(int, input().split()))

max_idx = li_a.index(max(li_a))

before, after = li_a[:max_idx], li_a[max_idx + 1:]
print(sum(before))
print(sum(after))
