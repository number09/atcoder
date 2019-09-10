n = int(input())
li_a = list(map(int, input().split()))

print(1 / (sum(1 / i for i in li_a)))