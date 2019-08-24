n = int(input())
li_m = list(map(int, input().split()))

print(sum(80 - m for m in li_m if m < 80))