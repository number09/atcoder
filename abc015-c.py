n, k = map(int, input().split())

li_t = list()
for i in range(n):
    li_t.append(list(map(int, input().split())))


def dfs(q_no, val):
    if q_no == n:
        return val == 0
    for i in range(k):
        if(dfs(q_no + 1, val ^ li_t[q_no][i])):
            return True
    return False

if dfs(0, 0):
    print("Found")
else:
    print("Nothing")

