n = int(input())
li_su = list(map(int, input().split()))

myset = set()
for i in sorted(li_su, reverse=True):
    work = i
    while True:
        if work % 2 == 0:
            work = work // 2
        else:
            myset.add(work)
            break

print(len(myset))
