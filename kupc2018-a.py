n = int(input())
li_s = list(map(int, input().split()))
li_a = list(map(int, input().split()))

print(max(s * a for s, a in zip(li_s, li_a)))
