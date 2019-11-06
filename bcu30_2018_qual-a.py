n = int(input())
li_a = list(map(int, input().split()))
print(" ".join([str(li_a.count(i)) for i in range(30)]))
