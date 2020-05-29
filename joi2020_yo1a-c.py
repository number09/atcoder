n, m = map(int, input().split())
li_a = list(map(int, input().split()))
li_b = list(map(int, input().split()))

for w in sorted(li_a + li_b):
    print(w)
