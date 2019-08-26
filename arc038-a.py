n = int(input())

li_a = list(map(int, input().split()))

print(sum(sorted(li_a, reverse=True)[::2]))